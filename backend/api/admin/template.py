from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Template


@admin.register(Template)
class TemplateAdmin(ModelAdmin):
    list_display = ["name", "company", "usage_count", "created_at", "updated_at"]
    list_filter = ["company", "created_at", "usage_count"]
    search_fields = ["name", "content", "trigger_keywords", "company__name"]
    readonly_fields = ["usage_count", "created_at", "updated_at"]
    autocomplete_fields = ["company"]
    fieldsets = (
        ("Company", {
            "fields": ("company",)
        }),
        ("Template Information", {
            "fields": ("name", "content")
        }),
        ("Configuration", {
            "fields": ("trigger_keywords",)
        }),
        ("Usage Statistics", {
            "fields": ("usage_count",)
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

