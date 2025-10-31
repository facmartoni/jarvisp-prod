from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import CompanyConfig


@admin.register(CompanyConfig)
class CompanyConfigAdmin(ModelAdmin):
    list_display = ["company", "max_tokens", "temperature", "updated_at"]
    list_filter = ["company"]
    search_fields = ["company__name", "system_prompt"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = [
        (
            "Company",
            {
                "fields": ["company"],
            },
        ),
        (
            "LLM Configuration",
            {
                "fields": ["system_prompt", "max_tokens", "temperature"],
            },
        ),
        (
            "Metadata",
            {
                "fields": ["created_at", "updated_at"],
            },
        ),
    ]

