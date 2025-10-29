from django.db import models


class KnowledgeBase(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        related_name="knowledge_base_entries",
    )
    question = models.TextField(help_text="Question or topic")
    answer = models.TextField(help_text="Answer or information")
    category = models.CharField(
        max_length=100,
        blank=True,
        help_text="Category for organization (e.g., 'billing', 'technical', 'general')"
    )
    keywords = models.JSONField(
        default=list,
        blank=True,
        help_text="Keywords for search and matching (array of strings)"
    )
    is_active = models.BooleanField(default=True, help_text="Whether this entry is active for bot use")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Knowledge Base Entry"
        verbose_name_plural = "Knowledge Base Entries"
        ordering = ["category", "-created_at"]
        indexes = [
            models.Index(fields=["company", "is_active"]),
            models.Index(fields=["company", "category"]),
        ]

    def __str__(self) -> str:
        preview = self.question[:60] + "..." if len(self.question) > 60 else self.question
        return f"[{self.category or 'Uncategorized'}] {preview}"

