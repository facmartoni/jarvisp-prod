"""
Unit tests for ISPCube client.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import httpx

from services.integrations.ispcube.client import ISPCubeClient
from services.integrations.ispcube.exceptions import (
    ISPCubeAPIError,
    ISPCubeAuthError,
)


@pytest.fixture
def ispcube_config():
    """Fixture providing ISPCube configuration."""
    return {
        "subdomain": "testcompany",
        "username": "api",
        "password": "testpass123",
        "api_key": "test-api-key-123",
        "client_id": "852",
        "base_url": "https://testcompany.ispcube.com",
    }


@pytest.fixture
def ispcube_client(ispcube_config):
    """Fixture providing ISPCube client instance."""
    return ISPCubeClient(ispcube_config)


class TestISPCubeClientInitialization:
    """Tests for ISPCube client initialization."""

    def test_client_initialization(self, ispcube_config):
        """Test that client initializes correctly with config."""
        client = ISPCubeClient(ispcube_config)

        assert client.base_url == "https://testcompany.ispcube.com"
        assert client.subdomain == "testcompany"
        assert client.username == "api"
        assert client.password == "testpass123"
        assert client.api_key == "test-api-key-123"
        assert client.client_id == "852"
        assert client._token is None
        assert client._token_expires_at is None

    def test_is_authenticated_without_token(self, ispcube_client):
        """Test is_authenticated returns False without token."""
        assert ispcube_client.is_authenticated is False

    def test_is_authenticated_with_valid_token(self, ispcube_client):
        """Test is_authenticated returns True with valid token."""
        ispcube_client._token = "valid-token"
        ispcube_client._token_expires_at = datetime.now() + timedelta(hours=1)

        assert ispcube_client.is_authenticated is True

    def test_is_authenticated_with_expired_token(self, ispcube_client):
        """Test is_authenticated returns False with expired token."""
        ispcube_client._token = "expired-token"
        ispcube_client._token_expires_at = datetime.now() - timedelta(hours=1)

        assert ispcube_client.is_authenticated is False


class TestISPCubeAuthentication:
    """Tests for ISPCube authentication."""

    @pytest.mark.asyncio
    async def test_successful_authentication_plain_text(self, ispcube_client):
        """Test successful authentication with plain text token (older ISPCube versions)."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "5|UdaQdRYxaOQfVSinqLbZIlUtuDinqt60WwWUGfGZ"
        mock_response.json.side_effect = Exception("Not JSON")

        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.return_value = mock_response

            result = await ispcube_client.authenticate()

            assert result["token"] == "5|UdaQdRYxaOQfVSinqLbZIlUtuDinqt60WwWUGfGZ"
            assert result["expires_in"] == 24
            assert ispcube_client._token == "5|UdaQdRYxaOQfVSinqLbZIlUtuDinqt60WwWUGfGZ"
            assert ispcube_client._token_expires_at is not None
            assert ispcube_client.is_authenticated is True

            # Verify the request was made correctly
            mock_post.assert_called_once()
            call_args = mock_post.call_args
            assert call_args[0][0] == "https://testcompany.ispcube.com/api/sanctum/token"
            assert call_args[1]["json"] == {
                "username": "api",
                "password": "testpass123",
            }
            assert call_args[1]["headers"]["api-key"] == "test-api-key-123"
            assert call_args[1]["headers"]["client-id"] == "852"
            assert call_args[1]["headers"]["login-type"] == "api"

    @pytest.mark.asyncio
    async def test_successful_authentication_json_response(self, ispcube_client):
        """Test successful authentication with JSON token (newer ISPCube versions)."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"token":"1382644|r5pSPm5k22WmKbp0J9OG2G"}'
        mock_response.json.return_value = {"token": "1382644|r5pSPm5k22WmKbp0J9OG2G"}

        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.return_value = mock_response

            result = await ispcube_client.authenticate()

            assert result["token"] == "1382644|r5pSPm5k22WmKbp0J9OG2G"
            assert result["expires_in"] == 24
            assert ispcube_client._token == "1382644|r5pSPm5k22WmKbp0J9OG2G"
            assert ispcube_client.is_authenticated is True

    @pytest.mark.asyncio
    async def test_authentication_with_invalid_credentials(self, ispcube_client):
        """Test authentication with invalid credentials."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"

        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.return_value = mock_response

            with pytest.raises(ISPCubeAuthError) as exc_info:
                await ispcube_client.authenticate()

            assert "Authentication failed" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_authentication_with_empty_token(self, ispcube_client):
        """Test authentication when API returns empty token."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = ""
        mock_response.json.side_effect = Exception("No JSON")

        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.return_value = mock_response

            with pytest.raises(ISPCubeAuthError) as exc_info:
                await ispcube_client.authenticate()

            assert "empty" in str(exc_info.value).lower()

    @pytest.mark.asyncio
    async def test_authentication_network_error(self, ispcube_client):
        """Test authentication with network error."""
        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.side_effect = httpx.RequestError("Connection failed")

            with pytest.raises(ISPCubeAPIError) as exc_info:
                await ispcube_client.authenticate()

            assert "Network error" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_authentication_server_error(self, ispcube_client):
        """Test authentication with server error."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"

        with patch.object(
            ispcube_client._http_client, "post", new_callable=AsyncMock
        ) as mock_post:
            mock_post.return_value = mock_response

            with pytest.raises(ISPCubeAPIError) as exc_info:
                await ispcube_client.authenticate()

            assert "Authentication request failed" in str(exc_info.value)
            assert exc_info.value.status_code == 500


class TestISPCubeTestConnection:
    """Tests for test_connection method."""

    @pytest.mark.asyncio
    async def test_connection_success(self, ispcube_client):
        """Test successful connection test."""
        with patch.object(
            ispcube_client, "authenticate", new_callable=AsyncMock
        ) as mock_auth:
            mock_auth.return_value = {"token": "test-token", "expires_in": 24}

            result = await ispcube_client.test_connection()

            assert result is True
            mock_auth.assert_called_once()

    @pytest.mark.asyncio
    async def test_connection_failure(self, ispcube_client):
        """Test failed connection test."""
        with patch.object(
            ispcube_client, "authenticate", new_callable=AsyncMock
        ) as mock_auth:
            mock_auth.side_effect = ISPCubeAuthError("Auth failed")

            result = await ispcube_client.test_connection()

            assert result is False


class TestISPCubeGetCustomers:
    """Tests for get_customers method."""

    @pytest.mark.asyncio
    async def test_get_customers_without_authentication(self, ispcube_client):
        """Test get_customers raises error when not authenticated."""
        # Mock authenticate to raise error to prevent actual network call
        with patch.object(
            ispcube_client, "authenticate", new_callable=AsyncMock
        ) as mock_auth:
            mock_auth.side_effect = ISPCubeAuthError("Not authenticated")

            with pytest.raises(ISPCubeAuthError):
                await ispcube_client.get_customers()

    @pytest.mark.asyncio
    async def test_get_customers_success(self, ispcube_client):
        """Test successful customer retrieval."""
        # Set up authenticated client
        ispcube_client._token = "valid-token"
        ispcube_client._token_expires_at = datetime.now() + timedelta(hours=1)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": 1,
                "code": "000001",
                "name": "Test Customer",
                "doc_number": "12345678",
            }
        ]

        with patch.object(
            ispcube_client._http_client, "get", new_callable=AsyncMock
        ) as mock_get:
            mock_get.return_value = mock_response

            customers = await ispcube_client.get_customers()

            assert len(customers) == 1
            assert customers[0]["code"] == "000001"
            assert customers[0]["name"] == "Test Customer"

            # Verify request parameters
            call_args = mock_get.call_args
            assert "customers/customers_list" in call_args[0][0]
            assert call_args[1]["params"]["limit"] == 25
            assert call_args[1]["params"]["offset"] == 0

    @pytest.mark.asyncio
    async def test_get_customers_with_filters(self, ispcube_client):
        """Test customer retrieval with filters."""
        ispcube_client._token = "valid-token"
        ispcube_client._token_expires_at = datetime.now() + timedelta(hours=1)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []

        with patch.object(
            ispcube_client._http_client, "get", new_callable=AsyncMock
        ) as mock_get:
            mock_get.return_value = mock_response

            await ispcube_client.get_customers(
                doc_number="12345678", limit=50, offset=100, deleted=True
            )

            call_args = mock_get.call_args
            params = call_args[1]["params"]
            assert params["doc_number"] == "12345678"
            assert params["limit"] == 50
            assert params["offset"] == 100
            assert params["deleted"] == "true"

    @pytest.mark.asyncio
    async def test_get_customers_expired_token(self, ispcube_client):
        """Test get_customers with expired token."""
        ispcube_client._token = "expired-token"
        ispcube_client._token_expires_at = datetime.now() - timedelta(hours=1)

        # Mock authenticate to be called by ensure_authenticated
        with patch.object(
            ispcube_client, "authenticate", new_callable=AsyncMock
        ) as mock_auth:
            mock_auth.return_value = {"token": "new-token", "expires_in": 24}

            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = []

            with patch.object(
                ispcube_client._http_client, "get", new_callable=AsyncMock
            ) as mock_get:
                mock_get.return_value = mock_response

                await ispcube_client.get_customers()

                # Should have re-authenticated
                mock_auth.assert_called_once()


class TestISPCubeContextManager:
    """Tests for async context manager."""

    @pytest.mark.asyncio
    async def test_context_manager(self, ispcube_config):
        """Test client works as async context manager."""
        async with ISPCubeClient(ispcube_config) as client:
            assert client is not None
            assert isinstance(client, ISPCubeClient)

        # Client should be closed after context
        # We can't easily test this without accessing internals

