from django.db import models

from api.constants import ConversationStatus


class Conversation(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.PROTECT,
        related_name="conversations",
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        related_name="conversations",
    )
    status = models.CharField(
        max_length=30,
        choices=ConversationStatus.choices,
        default=ConversationStatus.NEW,
    )
    started_at = models.DateTimeField(auto_now_add=True)
    last_message_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    total_messages = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conversation"
        verbose_name_plural = "Conversations"
        ordering = ["-last_message_at", "-started_at"]
        indexes = [
            models.Index(fields=["company", "customer", "is_active"]),
            models.Index(fields=["company", "last_message_at"]),
            models.Index(fields=["customer", "created_at"]),
            models.Index(fields=["company", "status"]),
        ]

    def __str__(self) -> str:
        return f"Conversation with {self.customer.name or self.customer.phone} - {self.get_status_display()}"  # type: ignore[misc]

