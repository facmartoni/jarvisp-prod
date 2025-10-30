import json
import logging

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
            return JsonResponse({"status": "ok"}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON received: {e}")
            return JsonResponse({"status": "ok"}, status=200)
        except Exception as e:
            logger.error(f"Error processing WhatsApp webhook: {e}")
            return JsonResponse({"status": "ok"}, status=200)

