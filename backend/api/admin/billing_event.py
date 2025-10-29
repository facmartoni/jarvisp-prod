from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import BillingEvent


@admin.register(BillingEvent)
class BillingEventAdmin(ModelAdmin):
    list_display = ["company", "event_type", "description_preview", "quantity", "unit_price", "total_amount", "period_start", "period_end", "created_at"]
    list_filter = ["event_type", "company", "period_start", "created_at"]
    search_fields = ["description", "company__name"]
    readonly_fields = ["total_amount", "created_at", "updated_at"]
    autocomplete_fields = ["company"]
    fieldsets = (
        ("Company", {
            "fields": ("company",)
        }),
        ("Event Details", {
            "fields": ("event_type", "description")
        }),
        ("Billing Calculations", {
            "fields": ("quantity", "unit_price", "total_amount")
        }),
        ("Period", {
            "fields": ("period_start", "period_end")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    @admin.display(description="Description")
    def description_preview(self, obj):
        """Display truncated description."""
        return obj.description[:60] + "..." if len(obj.description) > 60 else obj.description
