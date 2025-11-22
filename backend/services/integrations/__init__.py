"""
ISP Management System Integrations.

This package contains integrations with various LATAM ISP management systems
such as ISPCube, SmartOLT, Gestión Real, etc.

Usage:
    # Import base classes
    from services.integrations import BaseISPIntegration, IntegrationError
    
    # Import specific integrations
    from services.integrations.ispcube import ISPCubeClient
    from services.integrations.ispcube.service import get_company_ispcube_client
"""

from services.integrations.base import BaseISPIntegration, IntegrationError

__all__ = [
    "BaseISPIntegration",
    "IntegrationError",
]

