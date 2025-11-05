from django.db import models


class Sector(models.Model):
    """
    Sector model representing industry sectors (e.g., ISP, Retail, Healthcare).
    Used to define sector-level system prompts that apply to all companies in the sector.
    """

    name = models.CharField(max_length=100, unique=True)
    system_prompt = models.TextField(
        blank=True,
        help_text="General system prompt for this sector, applied to all companies in this sector",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name

