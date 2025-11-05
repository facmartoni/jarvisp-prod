from django.contrib import admin
from unfold.admin import ModelAdmin

from api.models import Company


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ["name", "slug", "sector", "whatsapp_phone_id", "timezone", "is_active", "created_at"]
    list_filter = ["is_active", "sector", "timezone", "created_at"]
    search_fields = ["name", "slug", "whatsapp_phone_id"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["created_at", "updated_at"]





