from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = ["conversation", "rating_display", "resolved_issue", "created_at"]
    list_filter = ["rating", "resolved_issue", "created_at"]
    search_fields = ["comment", "conversation__customer__name", "conversation__customer__phone"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["conversation"]
    fieldsets = (
        ("Conversation", {
            "fields": ("conversation",)
        }),
        ("Feedback", {
            "fields": ("rating", "comment", "resolved_issue")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    @admin.display(description="Rating")
    def rating_display(self, obj):
        """Display rating with stars."""
        return "⭐" * obj.rating + f" ({obj.rating}/5)"

