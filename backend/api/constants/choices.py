"""
Model field choices and enums.
"""

from django.db import models


class BillingEventType(models.TextChoices):
    """Event type choices for BillingEvent model."""
    SUBSCRIPTION = "subscription", "Subscription"
    OVERAGE = "overage", "Overage"


class MessageRole(models.TextChoices):
    """Role choices for Message model."""
    USER = "user", "User"
    ASSISTANT = "assistant", "Assistant (Bot)"
    AGENT = "agent", "Agent (Human)"
    SYSTEM = "system", "System"


class ConversationStatus(models.TextChoices):
    """
    Status choices for Conversation model in a customer service AI bot application.
    
    Flow:
    1. NEW → BOT_ACTIVE (bot handling)
    2. BOT_ACTIVE → AWAITING_CUSTOMER (waiting for reply)
    3. AWAITING_CUSTOMER → BOT_ACTIVE (customer responded)
    4. BOT_ACTIVE → ESCALATED (bot can't handle)
    5. ESCALATED → TRANSFERRED (assigned to human agent)
    6. TRANSFERRED → AGENT_ACTIVE (agent handling)
    7. AGENT_ACTIVE → RESOLVED (issue fixed)
    8. RESOLVED → CLOSED (conversation ended)
    """
    NEW = "new", "New"
    BOT_ACTIVE = "bot_active", "Bot Active"
    AWAITING_CUSTOMER = "awaiting_customer", "Awaiting Customer"
    ESCALATED = "escalated", "Escalated"
    TRANSFERRED = "transferred", "Transferred to Agent"
    AGENT_ACTIVE = "agent_active", "Agent Active"
    RESOLVED = "resolved", "Resolved"
    CLOSED = "closed", "Closed"
    ARCHIVED = "archived", "Archived"

