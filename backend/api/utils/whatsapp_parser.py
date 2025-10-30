import logging
from typing import TypedDict

logger = logging.getLogger(__name__)


class ParsedMessage(TypedDict):
    phone_number_id: str
    from_number: str
    message_body: str
    message_id: str


def parse_webhook_payload(data: dict) -> ParsedMessage | None:
    """
    Parse WhatsApp Cloud API webhook payload.

    Extracts phone_number_id, from_number, message_body, and message_id
    from incoming webhook notifications.

    Args:
        data: Webhook payload from WhatsApp Cloud API

    Returns:
        ParsedMessage dict if valid text message, None otherwise
    """
    try:
        # Navigate to the webhook structure
        entry = data.get("entry", [])
        if not entry:
            logger.warning("No entry field in webhook payload")
            return None

        changes = entry[0].get("changes", [])
        if not changes:
            logger.warning("No changes field in webhook payload")
            return None

        value = changes[0].get("value", {})

        # Extract metadata
        metadata = value.get("metadata", {})
        phone_number_id = metadata.get("phone_number_id")
        if not phone_number_id:
            logger.warning("No phone_number_id in webhook payload")
            return None

        # Extract messages
        messages = value.get("messages", [])
        if not messages:
            logger.debug("No messages field in webhook payload")
            return None

        message = messages[0]

        # Check if it's a text message
        message_type = message.get("type")
        if message_type != "text":
            logger.debug(f"Ignoring non-text message type: {message_type}")
            return None

        # Extract message fields
        from_number = message.get("from")
        message_id = message.get("id")
        text = message.get("text", {})
        message_body = text.get("body")

        # Validate required fields
        if not all([from_number, message_id, message_body]):
            logger.warning("Missing required fields in text message")
            return None

        return ParsedMessage(
            phone_number_id=phone_number_id,
            from_number=from_number,
            message_body=message_body,
            message_id=message_id,
        )

    except (KeyError, IndexError, TypeError) as e:
        logger.error(f"Error parsing webhook payload: {e}")
        return None

