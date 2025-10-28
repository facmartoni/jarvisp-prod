from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ["role", "content_preview", "conversation", "tokens_used", "latency_ms", "created_at"]
    list_filter = ["role", "created_at", "conversation__company"]
    search_fields = ["content", "conversation__customer__name", "conversation__customer__phone"]
    readonly_fields = ["created_at"]
    autocomplete_fields = ["conversation"]
    fieldsets = (
        ("Conversation", {
            "fields": ("conversation",)
        }),
        ("Message Content", {
            "fields": ("role", "content")
        }),
        ("Metrics", {
            "fields": ("tokens_used", "latency_ms")
        }),
        ("Timestamp", {
            "fields": ("created_at",)
        }),
    )

    @admin.display(description="Content Preview")
    def content_preview(self, obj):
        """Display truncated content."""
        return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content

