from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from api.constants import BillingEventType


class BillingEvent(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.PROTECT,
        related_name="billing_events",
    )
    event_type = models.CharField(
        max_length=20,
        choices=BillingEventType.choices,
    )
    description = models.TextField(help_text="Description of the billing event")
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Quantity of units"
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Price per unit"
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        help_text="Total amount (quantity × unit_price)"
    )
    period_start = models.DateField(help_text="Billing period start date")
    period_end = models.DateField(help_text="Billing period end date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Billing Event"
        verbose_name_plural = "Billing Events"
        ordering = ["-period_start", "-created_at"]
        indexes = [
            models.Index(fields=["company", "event_type"]),
            models.Index(fields=["company", "period_start", "period_end"]),
        ]

    def __str__(self) -> str:
        return f"{self.company.name} - {self.get_event_type_display()} (${self.total_amount})"  # type: ignore[misc]

    def save(self, *args, **kwargs):
        """Calculate total_amount if not provided."""
        if self.quantity and self.unit_price:
            self.total_amount = Decimal(self.quantity) * self.unit_price
        super().save(*args, **kwargs)
