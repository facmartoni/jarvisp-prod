import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def whatsapp_webhook(request):
    """
    WhatsApp Cloud API webhook endpoint.
    Receives and logs incoming webhook data from WhatsApp.
    """
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

