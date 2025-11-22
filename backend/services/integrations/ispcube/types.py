"""
Type definitions for ISPCube integration.
"""

from typing import TypedDict


class ISPCubeConfig(TypedDict):
    """
    Configuration for ISPCube integration.
    
    All values are provided by ISPCube staff when setting up API access.
    
    Attributes:
        subdomain: ISP's unique ISPCube subdomain (e.g., "myisp" from https://myisp.ispcube.com)
        username: API username provided by ISPCube staff
        password: API password provided by ISPCube staff
        api_key: Static API key provided by ISPCube staff
        client_id: Your company ID in ISPCube (referred to as "companyId" in their docs)
        base_url: Full ISPCube API base URL (e.g., "https://myisp.ispcube.com")
    """

    subdomain: str
    username: str
    password: str
    api_key: str
    client_id: str
    base_url: str


class ISPCubeAuthResponse(TypedDict):
    """Response from ISPCube authentication endpoint."""

    token: str
    expires_in: int  # Token validity in hours (24h for ISPCube)

