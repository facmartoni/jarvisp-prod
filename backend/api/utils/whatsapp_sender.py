import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_message(phone_number_id: str, to_number: str, text: str) -> bool:
    """
    Send a WhatsApp text message via the Cloud API.

    Args:
        phone_number_id: WhatsApp Business Phone Number ID
        to_number: Recipient's phone number (E.164 format)
        text: Message text content

    Returns:
        bool: True if message sent successfully, False otherwise
    """
    url = f"{settings.WHATSAPP_API_URL}/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to_number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": text,
        },
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()

        data = response.json()
        logger.info(
            f"Message sent successfully - To: {to_number}, "
            f"Message ID: {data.get('messages', [{}])[0].get('id', 'unknown')}"
        )
        return True

    except requests.exceptions.HTTPError as e:
        logger.error(
            f"HTTP error sending message - Status: {e.response.status_code}, "
            f"Response: {e.response.text}"
        )
        return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error sending message: {e}")
        return False

    except Exception as e:
        logger.error(f"Unexpected error sending message: {e}")
        return False

