from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import KnowledgeBase


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(ModelAdmin):
    list_display = ["question_preview", "category", "company", "is_active", "created_at"]
    list_filter = ["is_active", "category", "company", "created_at"]
    search_fields = ["question", "answer", "category", "keywords", "company__name"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["company"]
    fieldsets = (
        ("Company", {
            "fields": ("company",)
        }),
        ("Content", {
            "fields": ("question", "answer")
        }),
        ("Organization", {
            "fields": ("category", "keywords", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    @admin.display(description="Question")
    def question_preview(self, obj):
        """Display full question."""
        return obj.question

