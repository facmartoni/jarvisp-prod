from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import ToolCallLog


@admin.register(ToolCallLog)
class ToolCallLogAdmin(ModelAdmin):
    list_display = ["tool_name", "message", "success", "duration_ms", "created_at"]
    list_filter = ["success", "tool_name", "created_at"]
    search_fields = ["tool_name", "message__content", "message__conversation__customer__name"]
    readonly_fields = ["created_at"]
    autocomplete_fields = ["message"]
    fieldsets = (
        ("Message", {
            "fields": ("message",)
        }),
        ("Tool Information", {
            "fields": ("tool_name", "arguments", "response")
        }),
        ("Execution Metrics", {
            "fields": ("duration_ms", "success")
        }),
        ("Timestamp", {
            "fields": ("created_at",)
        }),
    )

