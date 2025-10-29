from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import AgentHandoff


@admin.register(AgentHandoff)
class AgentHandoffAdmin(ModelAdmin):
    list_display = ["reason_preview", "assigned_agent", "status_display", "created_at", "resolved_at"]
    list_filter = ["resolved_at", "assigned_agent", "created_at"]
    search_fields = ["reason", "notes", "assigned_agent", "conversation__customer__name"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["conversation"]
    fieldsets = (
        ("Conversation", {
            "fields": ("conversation",)
        }),
        ("Handoff Details", {
            "fields": ("reason", "assigned_agent")
        }),
        ("Resolution", {
            "fields": ("resolved_at", "notes")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    @admin.display(description="Reason")
    def reason_preview(self, obj):
        """Display truncated reason."""
        return obj.reason[:100] + "..." if len(obj.reason) > 100 else obj.reason

    @admin.display(description="Status", boolean=True)
    def status_display(self, obj):
        """Display whether handoff is resolved."""
        return obj.resolved_at is not None

