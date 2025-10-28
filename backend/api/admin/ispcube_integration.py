from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import ISPCubeIntegration


@admin.register(ISPCubeIntegration)
class ISPCubeIntegrationAdmin(ModelAdmin):
    list_display = ["company", "subdomain", "username", "is_active", "token_expires_at", "created_at"]
    list_filter = ["is_active", "created_at", "company"]
    search_fields = ["company__name", "subdomain", "username"]
    readonly_fields = ["created_at", "updated_at", "base_url"]
    fieldsets = (
        ("Company", {
            "fields": ("company",)
        }),
        ("ISPCube Configuration", {
            "fields": ("subdomain", "base_url", "username", "password", "api_key")
        }),
        ("Token Management", {
            "fields": ("api_token", "token_expires_at")
        }),
        ("Status", {
            "fields": ("is_active", "created_at", "updated_at")
        }),
    )

    @admin.display(description="Base URL")
    def base_url(self, obj):
        """Display the computed base URL."""
        return obj.base_url if obj.subdomain else "-"

