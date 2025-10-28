from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Customer


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ["name", "phone", "email", "company", "last_interaction", "created_at"]
    list_filter = ["company", "created_at", "last_interaction"]
    search_fields = ["name", "phone", "email", "external_id", "company__name"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        ("Company", {
            "fields": ("company",)
        }),
        ("Customer Information", {
            "fields": ("external_id", "name", "phone", "email")
        }),
        ("Interaction Data", {
            "fields": ("last_interaction", "metadata")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

