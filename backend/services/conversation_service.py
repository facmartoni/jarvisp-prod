import logging

import phonenumbers
from django.db import transaction
from django.utils import timezone

from api.constants import MessageRole
from api.models.company import Company
from api.models.conversation import Conversation
from api.models.customer import Customer
from api.models.message import Message

logger = logging.getLogger(__name__)


def handle_incoming_message(
    company: Company, from_number: str, message_body: str
) -> Message:
    """
    Handle incoming WhatsApp message by managing customer, conversation, and message creation.

    Args:
        company: The company receiving the message
        from_number: Customer's phone number (will be formatted to E.164)
        message_body: The text content of the message

    Returns:
        Message: The created message object
    """
    # Format phone number to E.164
    # Add + prefix if not present for phonenumbers library
    phone_to_parse = from_number if from_number.startswith('+') else f'+{from_number}'
    
    try:
        parsed = phonenumbers.parse(phone_to_parse, None)
        if phonenumbers.is_valid_number(parsed):
            e164_phone = phonenumbers.format_number(
                parsed, phonenumbers.PhoneNumberFormat.E164
            )
        else:
            logger.warning(f"Invalid phone number: {from_number}")
            e164_phone = phone_to_parse
    except phonenumbers.NumberParseException:
        logger.warning(f"Failed to parse phone number: {from_number}")
        e164_phone = phone_to_parse

    with transaction.atomic():
        # Get or create customer
        customer, created = Customer.objects.get_or_create(
            company=company,
            phone=e164_phone,
            defaults={"name": e164_phone},
        )

        if created:
            logger.info(f"Created new customer: {customer.phone}")

        # Update customer's last interaction
        customer.last_interaction = timezone.now()
        customer.save(update_fields=["last_interaction"])

        # Get or create active conversation with row-level locking
        conversation = (
            Conversation.objects.select_for_update()
            .filter(
                company=company,
                customer=customer,
                is_active=True,
            )
            .first()
        )

        if conversation is None:
            conversation = Conversation.objects.create(
                company=company,
                customer=customer,
                is_active=True,
            )
            logger.info(f"Created new conversation: {conversation.pk}")
        else:
            logger.info(f"Using existing conversation: {conversation.pk}")

        # Create message
        message = Message.objects.create(
            conversation=conversation,
            role=MessageRole.USER,
            content=message_body,
        )

        # Update conversation metadata
        conversation.last_message_at = timezone.now()
        conversation.total_messages += 1
        conversation.save(update_fields=["last_message_at", "total_messages"])

        logger.info(
            f"Message created - ID: {message.pk}, "
            f"Conversation: {conversation.pk}, "
            f"Customer: {customer.phone}"
        )

        return message


def get_conversation_history(conversation: Conversation, limit: int = 20) -> list[Message]:
    """
    Get conversation message history.

    Args:
        conversation: The conversation to retrieve messages from
        limit: Maximum number of messages to return (default 20)

    Returns:
        list[Message]: List of Message objects ordered by created_at
    """
    messages = Message.objects.filter(
        conversation=conversation
    ).order_by('-created_at')[:limit]

    return list(reversed(messages))


def save_assistant_message(
    conversation: Conversation,
    content: str,
    tokens_used: int = 0
) -> Message:
    """
    Save assistant message to conversation.

    Args:
        conversation: Conversation to add message to
        content: Message content
        tokens_used: Number of tokens used (default 0)

    Returns:
        Message: Created message object
    """
    message = Message.objects.create(
        conversation=conversation,
        role=MessageRole.ASSISTANT,
        content=content,
        tokens_used=tokens_used,
    )

    # Update conversation metadata
    conversation.last_message_at = timezone.now()
    conversation.total_messages += 1
    conversation.save(update_fields=["last_message_at", "total_messages"])

    logger.info(
        f"Assistant message saved - ID: {message.pk}, "
        f"Conversation: {conversation.pk}, "
        f"Tokens: {tokens_used}"
    )

    return message
