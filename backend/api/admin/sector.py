from django.contrib import admin

from api.models.sector import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (None, {"fields": ("name",)}),
        ("System Prompt", {"fields": ("system_prompt",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

