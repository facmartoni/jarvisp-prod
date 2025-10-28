from django.db import models

from api.constants import MessageRole


class Message(models.Model):
    conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    role = models.CharField(
        max_length=20,
        choices=MessageRole.choices,
    )
    content = models.TextField()
    tokens_used = models.PositiveIntegerField(default=0, help_text="Tokens consumed by this message")
    latency_ms = models.PositiveIntegerField(blank=True, null=True, help_text="Response latency in milliseconds")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["conversation", "created_at"]),
            models.Index(fields=["conversation", "role"]),
        ]

    def __str__(self) -> str:
        preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"{self.get_role_display()}: {preview}"  # type: ignore[misc]

