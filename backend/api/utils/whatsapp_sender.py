import logging
import re

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def format_argentina_whatsapp_number(phone: str) -> str:
    """
    Convert Argentina E.164 format to WhatsApp format.

    E.164: +5493816378744 or 5493816378744 (54 + 9 + area_code + number)
    WhatsApp: 54381156378744 (54 + area_code + 15 + number)

    Args:
        phone: Phone number in E.164 format

    Returns:
        str: Phone number in WhatsApp format, or original if not Argentina mobile
    """
    # Remove + if present
    phone = phone.lstrip('+')

    # Check if it's Argentina mobile (549 + 10 digits)
    if not re.match(r'^549\d{10}$', phone):
        return phone

    # Argentina mobile format: 549 + area_code + number (total 10 digits after 549)
    # Most area codes are 3 digits (11, 351, 381, etc.)
    match = re.match(r'^549(\d{3})(\d{7})$', phone)
    if match:
        area_code = match.group(1)
        number = match.group(2)
        whatsapp_format = f"54{area_code}15{number}"
        logger.debug(f"Converted {phone} → {whatsapp_format}")
        return whatsapp_format

    # Should never reach here if validation passed
    logger.warning(f"Failed to convert Argentina number: {phone}")
    return phone


def send_typing_indicator(phone_number_id: str, to_number: str, message_id: str) -> bool:
    """
    Mark message as read and show typing indicator.

    Args:
        phone_number_id: WhatsApp Business Phone Number ID
        to_number: Recipient's phone number (any format, will be converted for Argentina)
        message_id: WhatsApp message ID to mark as read

    Returns:
        bool: True if successful, False otherwise
    """
    # Convert Argentina numbers to WhatsApp format
    formatted_number = format_argentina_whatsapp_number(to_number)
    
    url = f"{settings.WHATSAPP_API_URL}/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "status": "read",
        "message_id": message_id,
        "typing_indicator": {
            "type": "text"
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Message marked as read - To: {formatted_number}")
        return True

    except requests.exceptions.HTTPError as e:
        logger.error(
            f"HTTP error marking message as read - Status: {e.response.status_code}, "
            f"Response: {e.response.text}"
        )
        return False

    except Exception as e:
        logger.warning(f"Failed to mark message as read: {e}")
        return False


def send_message(phone_number_id: str, to_number: str, text: str) -> bool:
    """
    Send a WhatsApp text message via the Cloud API.

    Args:
        phone_number_id: WhatsApp Business Phone Number ID
        to_number: Recipient's phone number (any format, will be converted for Argentina)
        text: Message text content

    Returns:
        bool: True if message sent successfully, False otherwise
    """
    # Convert Argentina numbers to WhatsApp format
    formatted_number = format_argentina_whatsapp_number(to_number)

    url = f"{settings.WHATSAPP_API_URL}/{phone_number_id}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": formatted_number,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": text,
        },
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()

        logger.info(f"Message sent successfully - To: {formatted_number}")
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
