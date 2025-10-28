"""
Custom Django fields for automatic encryption/decryption.
"""

from django.db import models

from api.utils.encryption import decrypt_value, encrypt_value


class EncryptedCharField(models.CharField):
    """
    CharField that automatically encrypts data before saving to database
    and decrypts when retrieving.
    """

    description = "Encrypted CharField"

    def get_prep_value(self, value):
        """Encrypt value before saving to database."""
        if value is None:
            return value
        # Convert to string if not already
        str_value = str(value) if not isinstance(value, str) else value
        if not str_value:
            return ""
        return encrypt_value(str_value)

    def from_db_value(self, value, expression, connection):
        """Decrypt value when retrieving from database."""
        if value is None:
            return value
        if not value:
            return ""
        return decrypt_value(value)

    def to_python(self, value):
        """Convert value to Python type."""
        if isinstance(value, str) or value is None:
            return value
        return str(value)


class EncryptedTextField(models.TextField):
    """
    TextField that automatically encrypts data before saving to database
    and decrypts when retrieving.
    """

    description = "Encrypted TextField"

    def get_prep_value(self, value):
        """Encrypt value before saving to database."""
        if value is None:
            return value
        str_value = str(value) if not isinstance(value, str) else value
        if not str_value:
            return ""
        return encrypt_value(str_value)

    def from_db_value(self, value, expression, connection):
        """Decrypt value when retrieving from database."""
        if value is None:
            return value
        if not value:
            return ""
        return decrypt_value(value)

    def to_python(self, value):
        """Convert value to Python type."""
        if isinstance(value, str) or value is None:
            return value
        return str(value)

