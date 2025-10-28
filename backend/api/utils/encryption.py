"""
Encryption utilities using Fernet (symmetric encryption).
"""

from cryptography.fernet import Fernet
from django.conf import settings


class EncryptionError(Exception):
    """Raised when encryption/decryption operations fail."""
    pass


def get_fernet() -> Fernet:
    """
    Get Fernet instance using the encryption key from settings.

    Raises:
        EncryptionError: If ENCRYPTION_KEY is not configured.
    """
    encryption_key = getattr(settings, "ENCRYPTION_KEY", None)

    if not encryption_key:
        raise EncryptionError(
            "ENCRYPTION_KEY not found in settings. "
            "Generate one with: python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'"
        )

    try:
        return Fernet(encryption_key.encode() if isinstance(encryption_key, str) else encryption_key)
    except Exception as e:
        raise EncryptionError(f"Invalid ENCRYPTION_KEY: {e}") from e


def encrypt_value(value: str) -> str:
    """
    Encrypt a string value.

    Args:
        value: Plain text string to encrypt.

    Returns:
        Encrypted string (base64 encoded).
    """
    if not value:
        return ""

    fernet = get_fernet()
    encrypted = fernet.encrypt(value.encode())
    return encrypted.decode()


def decrypt_value(encrypted_value: str) -> str:
    """
    Decrypt an encrypted string value.

    Args:
        encrypted_value: Encrypted string (base64 encoded).

    Returns:
        Decrypted plain text string.

    Raises:
        EncryptionError: If decryption fails.
    """
    if not encrypted_value:
        return ""

    try:
        fernet = get_fernet()
        decrypted = fernet.decrypt(encrypted_value.encode())
        return decrypted.decode()
    except Exception as e:
        raise EncryptionError(f"Failed to decrypt value: {e}") from e

