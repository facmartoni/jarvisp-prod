from django.db import models


class Customer(models.Model):
    company = models.ForeignKey(
        "Company",
        on_delete=models.PROTECT, # When a company is deleted, we don't want to delete the customers
        related_name="customers",
    )
    external_id = models.CharField(max_length=255, help_text="External system identifier")
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True, help_text="Additional flexible data")
    last_interaction = models.DateTimeField(blank=True, null=True, help_text="Last interaction timestamp")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["-last_interaction", "-created_at"]
        unique_together = [["company", "external_id"]]
        indexes = [
            models.Index(fields=["company", "phone"]),
            models.Index(fields=["company", "email"]),
            models.Index(fields=["last_interaction"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.phone})"

