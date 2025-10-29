from django.db import models


class Template(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        related_name="templates",
    )
    name = models.CharField(max_length=255, help_text="Template name for identification")
    content = models.TextField(help_text="Template content/message")
    trigger_keywords = models.JSONField(
        default=list,
        blank=True,
        help_text="Keywords that trigger this template (array of strings)"
    )
    usage_count = models.PositiveIntegerField(default=0, help_text="Number of times this template has been used")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"
        ordering = ["-usage_count", "name"]
        indexes = [
            models.Index(fields=["company", "usage_count"]),
        ]
        unique_together = [["company", "name"]]

    def __str__(self) -> str:
        return f"{self.name} (used {self.usage_count} times)"

