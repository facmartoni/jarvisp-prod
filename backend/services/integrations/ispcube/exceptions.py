"""
ISPCube-specific exceptions.
"""

from services.integrations.base import APIError, AuthenticationError, IntegrationError


class ISPCubeError(IntegrationError):
    """Base exception for ISPCube-specific errors."""

    pass


class ISPCubeAuthError(AuthenticationError):
    """ISPCube authentication failed."""

    pass


class ISPCubeAPIError(APIError):
    """ISPCube API request failed."""

    pass


class ISPCubeValidationError(ISPCubeError):
    """ISPCube request validation failed."""

    pass

