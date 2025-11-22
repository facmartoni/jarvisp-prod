"""
Service layer for ISPCube integration.

This module provides helper functions to work with ISPCube integration
and Django models.
"""

from api.models.ispcube_integration import ISPCubeIntegration


from typing import Optional

from django.core.exceptions import ObjectDoesNotExist

from api.models import Company, ISPCubeIntegration
from services.integrations.ispcube.client import ISPCubeClient
from services.integrations.ispcube.exceptions import ISPCubeError
from services.integrations.ispcube.types import ISPCubeConfig


def get_ispcube_config(integration: ISPCubeIntegration) -> ISPCubeConfig:
    """
    Convert ISPCubeIntegration model to client configuration.

    Args:
        integration: ISPCubeIntegration model instance

    Returns:
        Configuration dictionary for ISPCubeClient

    Note:
        Encrypted fields (password, api_key) are automatically decrypted
        when accessed through the model.
    """
    return {
        "subdomain": integration.subdomain,
        "username": integration.username,
        "password": integration.password,  # Auto-decrypted by EncryptedCharField
        "api_key": integration.api_key,  # Auto-decrypted by EncryptedCharField
        "client_id": str(integration.company.id),
        "base_url": integration.base_url,
    }


def get_ispcube_client(integration: ISPCubeIntegration) -> ISPCubeClient:
    """
    Create ISPCube client from integration model.

    Args:
        integration: ISPCubeIntegration model instance

    Returns:
        Configured ISPCubeClient instance

    Example:
        >>> integration = ISPCubeIntegration.objects.get(company=company)
        >>> async with get_ispcube_client(integration) as client:
        ...     await client.authenticate()
        ...     customers = await client.get_customers()
    """
    config = get_ispcube_config(integration)
    return ISPCubeClient(config)


def get_company_ispcube_client(company: Company, subdomain: Optional[str] = None) -> ISPCubeClient:
    """
    Get ISPCube client for a company.

    Args:
        company: Company instance
        subdomain: Optional subdomain filter (if company has multiple integrations)

    Returns:
        Configured ISPCubeClient instance

    Raises:
        ObjectDoesNotExist: If no active integration found for company
        ISPCubeError: If multiple integrations found and no subdomain specified

    Example:
        >>> company = Company.objects.get(id=1)
        >>> async with get_company_ispcube_client(company) as client:
        ...     await client.authenticate()
        ...     customers = await client.get_customers()
    """
    query = ISPCubeIntegration.objects.filter(company=company, is_active=True)

    if subdomain:
        query = query.filter(subdomain=subdomain)

    integrations = list[ISPCubeIntegration](query)

    if not integrations:
        raise ObjectDoesNotExist(
            f"No active ISPCube integration found for company {company.name}"
        )

    if len(integrations) > 1 and not subdomain:
        raise ISPCubeError(
            f"Company {company.name} has multiple ISPCube integrations. "
            "Please specify subdomain."
        )

    return get_ispcube_client(integrations[0])


async def validate_ispcube_integration(integration: ISPCubeIntegration) -> tuple[bool, Optional[str]]:
    """
    Test ISPCube integration connection.

    Args:
        integration: ISPCubeIntegration model instance

    Returns:
        Tuple of (success: bool, error_message: Optional[str])

    Example:
        >>> integration = ISPCubeIntegration.objects.get(id=1)
        >>> if success:
        ...     print("Connection successful!")
        ... else:
        ...     print(f"Connection failed: {error}")
    """
    try:
        async with get_ispcube_client(integration) as client:
            success = await client.test_connection()
            if success:
                return True, None
            return False, "Connection test failed"
    except Exception as e:
        return False, str(e)

