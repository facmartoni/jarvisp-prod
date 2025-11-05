from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CompanyConfig(models.Model):
    company = models.OneToOneField(
        "Company",
        on_delete=models.CASCADE,
        related_name="config",
    )
    system_prompt = models.TextField(
        default="Sos un asistente de soporte para {company_name}. Ayudás con consultas sobre servicio de Internet. Sé amable y profesional.",
        help_text="System prompt for the AI assistant. Use {company_name} as placeholder."
    )
    max_tokens = models.PositiveIntegerField(
        default=500,
        validators=[MinValueValidator(1), MaxValueValidator(8192)],
        help_text="Maximum tokens for AI response"
    )
    temperature = models.FloatField(
        default=0.7,
        validators=[MinValueValidator(0.0), MaxValueValidator(2.0)],
        help_text="Creativity level (0.0-2.0). Lower is more focused, higher is more creative."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Configuration"
        verbose_name_plural = "Company Configurations"

    def __str__(self) -> str:
        return f"{self.company.name} - Config"

    def get_system_prompt(self) -> str:
        """
        Get system prompt with company name interpolated.
        If company has a sector with system_prompt, prepends sector prompt.
        """
        # Start with company-specific prompt
        company_prompt = self.system_prompt.replace("{company_name}", self.company.name)
        
        # Prepend sector prompt if available
        if self.company.sector and self.company.sector.system_prompt:
            sector_prompt = self.company.sector.system_prompt
            return f"{sector_prompt}\n\n{company_prompt}"
        
        return company_prompt

