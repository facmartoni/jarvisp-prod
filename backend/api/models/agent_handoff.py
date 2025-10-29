from django.db import models


class AgentHandoff(models.Model):
    conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.PROTECT,
        related_name="agent_handoffs",
    )
    reason = models.TextField(help_text="Reason for escalation to human agent")
    assigned_agent = models.CharField(
        max_length=255,
        blank=True,
        help_text="Name or ID of assigned agent"
    )
    resolved_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the agent resolved the issue"
    )
    notes = models.TextField(
        blank=True,
        help_text="Additional notes or resolution details"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agent Handoff"
        verbose_name_plural = "Agent Handoffs"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["conversation", "created_at"]),
            models.Index(fields=["assigned_agent", "resolved_at"]),
        ]

    def __str__(self) -> str:
        status = "Resolved" if self.resolved_at else "Pending"
        agent = self.assigned_agent or "Unassigned"
        return f"{agent} - {status}"

