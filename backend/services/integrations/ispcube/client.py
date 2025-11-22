"""
ISPCube API Client.

This module provides the main client for interacting with ISPCube's API.
"""

import logging
from datetime import datetime, timedelta
from typing import Any, Optional

import httpx

from services.integrations.base import BaseISPIntegration
from services.integrations.ispcube.exceptions import (
    ISPCubeAPIError,
    ISPCubeAuthError,
)
from services.integrations.ispcube.types import ISPCubeAuthResponse, ISPCubeConfig

logger = logging.getLogger(__name__)


class ISPCubeClient(BaseISPIntegration):
    """
    Client for ISPCube API integration.

    This client handles authentication, token management, and API requests
    to ISPCube's management system.

    Example:
        >>> # All config values provided by ISPCube staff
        >>> config = {
        ...     "subdomain": "myisp",  # From your ISPCube URL
        ...     "username": "api",
        ...     "password": "your-password-here",
        ...     "api_key": "your-api-key-uuid-here",
        ...     "client_id": "123",  # Your company ID in ISPCube
        ...     "base_url": "https://myisp.ispcube.com"
        ... }
        >>> client = ISPCubeClient(config)
        >>> await client.authenticate()
        >>> customers = await client.get_customers()
    """

    TOKEN_VALIDITY_HOURS = 24  # ISPCube tokens are valid for 24 hours

    def __init__(self, config: ISPCubeConfig):
        """
        Initialize ISPCube client.

        Args:
            config: ISPCube configuration dictionary
        """
        super().__init__(config)
        self.base_url = config["base_url"]
        self.subdomain = config["subdomain"]
        self.username = config["username"]
        self.password = config["password"]
        self.api_key = config["api_key"]
        self.client_id = config["client_id"]

        # HTTP client with reasonable defaults
        self._http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
        )

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._http_client.aclose()

    def _get_auth_headers(self) -> dict[str, str]:
        """
        Get headers required for authentication endpoint.

        Returns:
            Dictionary of headers for login request
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "api-key": self.api_key,
            "client-id": self.client_id,
            "login-type": "api",
        }

    def _get_api_headers(self) -> dict[str, str]:
        """
        Get headers required for authenticated API requests.

        Returns:
            Dictionary of headers for API requests

        Raises:
            ISPCubeAuthError: If not authenticated
        """
        if not self._token:
            raise ISPCubeAuthError("Not authenticated. Call authenticate() first.")

        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "api-key": self.api_key,
            "client-id": self.client_id,
            "login-type": "api",
            "username": self.username,
            "Authorization": f"Bearer {self._token}",
        }

    async def authenticate(self) -> ISPCubeAuthResponse:
        """
        Authenticate with ISPCube API and obtain access token.

        The token is valid for 24 hours according to ISPCube documentation.
        
        Note: ISPCube API may return the token in different formats:
        - Newer versions: JSON object {"token": "..."}
        - Older versions: Plain text token
        This method handles both formats automatically.

        Returns:
            Dictionary containing token and expiration info

        Raises:
            ISPCubeAuthError: If authentication fails
            ISPCubeAPIError: If API request fails
        """
        url = f"{self.base_url}/api/sanctum/token"
        payload = {
            "username": self.username,
            "password": self.password,
        }

        logger.info(f"Authenticating with ISPCube at {self.subdomain}")

        try:
            response = await self._http_client.post(
                url, json=payload, headers=self._get_auth_headers()
            )

            if response.status_code == 401:
                raise ISPCubeAuthError(
                    "Authentication failed. Check credentials and API key."
                )

            if response.status_code != 200:
                raise ISPCubeAPIError(
                    f"Authentication request failed with status {response.status_code}",
                    status_code=response.status_code,
                    response=response.text,
                )

            # ISPCube returns the token as JSON or plain text depending on version
            response_text = response.text.strip()
            
            if not response_text:
                raise ISPCubeAuthError("Authentication returned empty response")
            
            # Try to parse as JSON first (newer ISPCube versions)
            try:
                response_data = response.json()
                if isinstance(response_data, dict) and "token" in response_data:
                    token = response_data["token"]
                else:
                    # Fallback to plain text response
                    token = response_text
            except Exception:
                # Plain text token (older ISPCube versions)
                token = response_text

            if not token:
                raise ISPCubeAuthError("Authentication returned empty token")

            # Store token and expiration
            self._token = token
            self._token_expires_at = datetime.now() + timedelta(
                hours=self.TOKEN_VALIDITY_HOURS
            )

            logger.info(f"Successfully authenticated with ISPCube ({self.subdomain})")
            logger.debug(f"Token expires at: {self._token_expires_at}")

            return {
                "token": token,
                "expires_in": self.TOKEN_VALIDITY_HOURS,
            }

        except httpx.RequestError as e:
            raise ISPCubeAPIError(f"Network error during authentication: {str(e)}")

    async def test_connection(self) -> bool:
        """
        Test the connection to ISPCube API.

        This method attempts to authenticate and verifies the connection works.

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            await self.authenticate()
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {str(e)}")
            return False

    async def get_customers(
        self,
        doc_number: Optional[str] = None,
        limit: int = 25,
        offset: int = 0,
        deleted: bool = False,
        temporary: bool = False,
    ) -> list[dict[str, Any]]:
        """
        Retrieve customers from ISPCube.

        Args:
            doc_number: Filter by document number (DNI/CUIT/CUIL/RUT)
            limit: Number of records per request (max 100)
            offset: Starting offset for pagination
            deleted: Include deleted customers
            temporary: Include temporary customers

        Returns:
            List of customer dictionaries

        Raises:
            ISPCubeAuthError: If not authenticated
            ISPCubeAPIError: If API request fails
        """
        await self.ensure_authenticated()

        url = f"{self.base_url}/api/customers/customers_list"
        params = {
            "limit": min(limit, 100),  # ISPCube max is 100
            "offset": offset,
        }

        if doc_number:
            params["doc_number"] = doc_number
        if deleted:
            params["deleted"] = "true"
        if temporary:
            params["temporary"] = "true"

        try:
            response = await self._http_client.get(
                url, params=params, headers=self._get_api_headers()
            )

            if response.status_code == 401:
                # Token expired, clear it and raise
                self._token = None
                raise ISPCubeAuthError("Token expired or invalid")

            if response.status_code != 200:
                raise ISPCubeAPIError(
                    f"Get customers failed with status {response.status_code}",
                    status_code=response.status_code,
                    response=response.text,
                )

            customers = response.json()
            logger.info(f"Retrieved {len(customers)} customers from ISPCube")

            return customers

        except httpx.RequestError as e:
            raise ISPCubeAPIError(f"Network error while fetching customers: {str(e)}")

