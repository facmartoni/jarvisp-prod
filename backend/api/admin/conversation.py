from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Conversation


@admin.register(Conversation)
class ConversationAdmin(ModelAdmin):
    list_display = ["customer", "company", "status", "total_messages", "last_message_at", "is_active", "started_at"]
    list_filter = ["status", "is_active", "company", "started_at", "last_message_at"]
    search_fields = ["customer__name", "customer__phone", "customer__email", "company__name"]
    readonly_fields = ["started_at", "created_at", "updated_at"]
    autocomplete_fields = ["customer"]
    fieldsets = (
        ("Participants", {
            "fields": ("company", "customer")
        }),
        ("Status", {
            "fields": ("status", "is_active")
        }),
        ("Metrics", {
            "fields": ("total_messages", "started_at", "last_message_at")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

