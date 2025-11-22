"""
Base classes for ISP management system integrations.

This module defines the abstract base classes and common interfaces
that all ISP integrations must implement.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional


class IntegrationError(Exception):
    """Base exception for integration errors."""

    pass


class AuthenticationError(IntegrationError):
    """Raised when authentication fails."""

    pass


class APIError(IntegrationError):
    """Raised when API request fails."""

    def __init__(
        self, message: str, status_code: Optional[int] = None, response: Optional[Any] = None
    ):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class TokenExpiredError(AuthenticationError):
    """Raised when token has expired."""

    pass


class BaseISPIntegration(ABC):
    """
    Abstract base class for ISP management system integrations.

    All ISP integrations must inherit from this class and implement
    the required methods.
    """

    def __init__(self, config: dict[str, Any]):
        """
        Initialize the integration with configuration.

        Args:
            config: Dictionary containing integration configuration
                   (credentials, endpoints, etc.)
        """
        self.config = config
        self._token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None

    @property
    def is_authenticated(self) -> bool:
        """Check if integration has valid authentication."""
        if not self._token:
            return False
        if self._token_expires_at and datetime.now() >= self._token_expires_at:
            return False
        return True

    @abstractmethod
    async def authenticate(self) -> dict[str, Any]:
        """
        Authenticate with the ISP management system.

        Returns:
            Dictionary containing authentication response with token info

        Raises:
            AuthenticationError: If authentication fails
        """
        pass

    @abstractmethod
    async def test_connection(self) -> bool:
        """
        Test the connection to the ISP management system.

        Returns:
            True if connection is successful, False otherwise
        """
        pass

    async def ensure_authenticated(self) -> None:
        """Ensure we have valid authentication, refresh if needed."""
        if not self.is_authenticated:
            await self.authenticate()

