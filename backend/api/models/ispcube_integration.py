from django.db import models

from api.fields import EncryptedCharField, EncryptedTextField


class ISPCubeIntegration(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        related_name="ispcube_integrations",
    )
    subdomain = models.CharField(
        max_length=255,
        help_text="ISPCube subdomain from your login URL (e.g., 'online24' for https://online24.ispcube.com). Provided by ISPCube staff."
    )
    username = models.CharField(
        max_length=255,
        help_text="API username provided by ISPCube staff"
    )
    password = EncryptedCharField(
        max_length=500,
        help_text="API password provided by ISPCube staff (stored encrypted)"
    )
    api_key = EncryptedCharField(
        max_length=500,
        help_text="Static API key provided by ISPCube staff (stored encrypted)"
    )
    api_token = EncryptedTextField(
        blank=True,
        null=True,
        help_text="Dynamic bearer token obtained from authentication (stored encrypted, refreshed every 24h)"
    )
    token_expires_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Token expiration timestamp (ISPCube tokens are valid for 24 hours)"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ISPCube Integration"
        verbose_name_plural = "ISPCube Integrations"
        ordering = ["-created_at"]
        unique_together = [["company", "subdomain"]]

    def __str__(self) -> str:
        return f"{self.company.name} - {self.subdomain}"

    @property
    def base_url(self) -> str:
        """Returns the base URL for ISPCube API calls."""
        return f"https://{self.subdomain}.ispcube.com"

