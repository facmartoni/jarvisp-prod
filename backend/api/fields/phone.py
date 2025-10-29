"""
Custom Django field for E.164 phone number validation and formatting.
"""

import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone_number(value):
    """
    Validate that the phone number is valid and can be parsed.
    Accepts various formats including E.164.
    """
    if not value:
        return

    try:
        # Parse the phone number (handles E.164 and other formats)
        parsed = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed):
            raise ValidationError(
                f"'{value}' is not a valid phone number.",
                code="invalid_phone"
            )
    except phonenumbers.NumberParseException as e:
        raise ValidationError(
            f"'{value}' is not a valid phone number: {str(e)}",
            code="invalid_phone"
        ) from e


class E164PhoneNumberField(models.CharField):
    """
    CharField that validates and stores phone numbers in E.164 format.
    
    E.164 format: +[country code][number] (e.g., +5491112345678)
    """
    
    description = "E.164 formatted phone number"
    default_validators = [validate_phone_number]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 20)
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        """Convert phone number to E.164 format before saving."""
        if not value:
            return value

        try:
            parsed = phonenumbers.parse(value, None)
            if phonenumbers.is_valid_number(parsed):
                # Convert to E.164 format
                return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            pass

        # If parsing fails, return as-is and let validation handle it
        return value

    def to_python(self, value):
        """Convert value to Python type."""
        if isinstance(value, str) or value is None:
            return value
        return str(value)

