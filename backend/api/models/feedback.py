from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Feedback(models.Model):
    conversation = models.OneToOneField(
        "Conversation",
        on_delete=models.CASCADE,
        related_name="feedback",
        primary_key=True,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 (poor) to 5 (excellent)"
    )
    comment = models.TextField(blank=True, help_text="Customer feedback comments")
    resolved_issue = models.BooleanField(default=False, help_text="Whether the issue was resolved")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["rating", "resolved_issue"]),
        ]

    def __str__(self) -> str:
        stars = "⭐" * self.rating
        resolved = "✓" if self.resolved_issue else "✗"
        return f"{stars} ({self.rating}/5) - Resolved: {resolved}"

