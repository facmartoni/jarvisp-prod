from django.db import models


class ToolCallLog(models.Model):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        related_name="tool_calls",
    )
    tool_name = models.CharField(max_length=255, help_text="Name of the tool/function called")
    arguments = models.JSONField(help_text="Arguments passed to the tool")
    response = models.JSONField(help_text="Response received from the tool")
    duration_ms = models.PositiveIntegerField(help_text="Execution duration in milliseconds")
    success = models.BooleanField(default=True, help_text="Whether the tool call succeeded")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tool Call Log"
        verbose_name_plural = "Tool Call Logs"
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["message", "created_at"]),
            models.Index(fields=["tool_name", "success"]),
        ]

    def __str__(self) -> str:
        status = "✓" if self.success else "✗"
        return f"{status} {self.tool_name} ({self.duration_ms}ms)"

