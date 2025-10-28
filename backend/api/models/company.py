from django.db import models

from api.constants import LATAM_TIMEZONES


class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    whatsapp_phone_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    timezone = models.CharField(max_length=50, choices=LATAM_TIMEZONES, default="America/Argentina/Buenos_Aires")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name

