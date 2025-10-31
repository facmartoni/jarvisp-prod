import json
import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models.company import Company
from api.utils.whatsapp_parser import parse_webhook_payload
from api.utils.whatsapp_sender import send_message
from services.conversation_service import (
    get_conversation_history,
    handle_incoming_message,
    save_assistant_message,
)
from services.llm_service import format_messages_for_gemini, generate_response

logger = logging.getLogger(__name__)


@csrf_exempt
def whatsapp_webhook(request):
    """
    WhatsApp Cloud API webhook endpoint.
    GET: Webhook verification
    POST: Receives and logs incoming webhook data from WhatsApp.
    """
    if request.method == "GET":
        # Webhook verification
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == settings.WHATSAPP_VERIFY_TOKEN:
            logger.info("WhatsApp webhook verified successfully")
            return HttpResponse(challenge, content_type="text/plain")
        else:
            logger.warning("WhatsApp webhook verification failed")
            return HttpResponseForbidden()

    elif request.method == "POST":
        # Handle incoming webhook data
        try:
            data = json.loads(request.body)
            logger.info(f"WhatsApp webhook received: {json.dumps(data, indent=2)}")

            # Parse the webhook payload
            parsed = parse_webhook_payload(data)
            if parsed:
                logger.info(
                    f"Parsed message - From: {parsed['from_number']}, "
                    f"Body: {parsed['message_body']}, "
                    f"ID: {parsed['message_id']}"
                )

                # Query Company by whatsapp_phone_id
                try:
                    company = Company.objects.get(
                        whatsapp_phone_id=parsed["phone_number_id"]
                    )
                    request.company = company
                    logger.info(f"Company found: {company.name}")

                    # Handle incoming message
                    user_message = handle_incoming_message(
                        company=company,
                        from_number=parsed["from_number"],
                        message_body=parsed["message_body"],
                    )
                    logger.info(f"Message handled successfully: {user_message.pk}")

                    # Generate AI response
                    try:
                        # Get conversation history
                        history = get_conversation_history(
                            user_message.conversation, limit=20
                        )

                        # Format for Gemini (exclude the just-created user_message)
                        formatted_history = format_messages_for_gemini(history[:-1])

                        # Generate response
                        response_text, tokens_used = generate_response(
                            company=company,
                            conversation_history=formatted_history,
                            user_message=parsed["message_body"],
                        )
                        logger.info(
                            f"AI response generated: {response_text[:100]} "
                            f"(tokens: {tokens_used})"
                        )

                    except Exception as e:
                        # Fallback message on LLM error
                        logger.error(f"LLM generation error: {e}", exc_info=True)
                        response_text = (
                            "Disculpá, estoy teniendo problemas técnicos. "
                            "Por favor, intentá de nuevo en unos minutos."
                        )
                        tokens_used = 0

                    # Send response via WhatsApp
                    success = send_message(
                        phone_number_id=parsed["phone_number_id"],
                        to_number=parsed["from_number"],
                        text=response_text,
                    )

                    if success:
                        # Save assistant message to database
                        assistant_message = save_assistant_message(
                            conversation=user_message.conversation,
                            content=response_text,
                            tokens_used=tokens_used,
                        )
                        logger.info(
                            f"Assistant message sent and saved: {assistant_message.pk}"
                        )
                    else:
                        logger.error("Failed to send WhatsApp message")

                except Company.DoesNotExist:
                    logger.error(
                        f"Company not found for phone_number_id: {parsed['phone_number_id']}"
                    )
                    return JsonResponse({"status": "ok"}, status=200)

            return JsonResponse({"status": "ok"}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON received: {e}")
            return JsonResponse({"status": "ok"}, status=200)
        except Exception as e:
            logger.error(f"Error processing WhatsApp webhook: {e}")
            return JsonResponse({"status": "ok"}, status=200)

