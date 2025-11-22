"""
Unit tests for ISPCube service layer.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from django.core.exceptions import ObjectDoesNotExist

from services.integrations.ispcube.exceptions import ISPCubeError
from services.integrations.ispcube.service import (
    get_company_ispcube_client,
    get_ispcube_client,
    get_ispcube_config,
    validate_ispcube_integration,
)


@pytest.fixture
def mock_company():
    """Fixture providing mock Company instance."""
    company = MagicMock()
    company.id = 1
    company.name = "Test Company"
    return company


@pytest.fixture
def mock_integration(mock_company):
    """Fixture providing mock ISPCubeIntegration instance."""
    integration = MagicMock()
    integration.company = mock_company
    integration.subdomain = "testcompany"
    integration.username = "api"
    integration.password = "testpass123"
    integration.api_key = "test-api-key"
    integration.base_url = "https://testcompany.ispcube.com"
    integration.is_active = True
    return integration


class TestGetISPCubeConfig:
    """Tests for get_ispcube_config function."""

    def test_get_config_from_integration(self, mock_integration):
        """Test config generation from integration model."""
        config = get_ispcube_config(mock_integration)

        assert config["subdomain"] == "testcompany"
        assert config["username"] == "api"
        assert config["password"] == "testpass123"
        assert config["api_key"] == "test-api-key"
        assert config["client_id"] == "1"
        assert config["base_url"] == "https://testcompany.ispcube.com"


class TestGetISPCubeClient:
    """Tests for get_ispcube_client function."""

    def test_get_client_from_integration(self, mock_integration):
        """Test client creation from integration model."""
        client = get_ispcube_client(mock_integration)

        assert client.subdomain == "testcompany"
        assert client.username == "api"
        assert client.base_url == "https://testcompany.ispcube.com"


class TestGetCompanyISPCubeClient:
    """Tests for get_company_ispcube_client function."""

    def test_get_client_for_company_with_single_integration(self, mock_company, mock_integration):
        """Test getting client when company has single integration."""
        with patch("services.integrations.ispcube.service.ISPCubeIntegration") as mock_model:
            # Mock the query chain properly
            mock_query = MagicMock()
            mock_query.__iter__ = MagicMock(return_value=iter([mock_integration]))
            mock_model.objects.filter.return_value = mock_query

            client = get_company_ispcube_client(mock_company)

            assert client is not None
            assert client.subdomain == "testcompany"

    def test_get_client_for_company_with_subdomain_filter(
        self, mock_company, mock_integration
    ):
        """Test getting client with subdomain filter."""
        with patch("services.integrations.ispcube.service.ISPCubeIntegration") as mock_model:
            mock_query = MagicMock()
            mock_query.filter.return_value = [mock_integration]
            mock_model.objects.filter.return_value = mock_query

            client = get_company_ispcube_client(mock_company, subdomain="testcompany")

            assert client is not None
            mock_query.filter.assert_called_once_with(subdomain="testcompany")

    def test_get_client_for_company_no_integration(self, mock_company):
        """Test error when company has no integration."""
        with patch("services.integrations.ispcube.service.ISPCubeIntegration") as mock_model:
            mock_model.objects.filter.return_value.filter.return_value = []

            with pytest.raises(ObjectDoesNotExist) as exc_info:
                get_company_ispcube_client(mock_company)

            assert "No active ISPCube integration found" in str(exc_info.value)

    def test_get_client_for_company_multiple_integrations_no_subdomain(
        self, mock_company, mock_integration
    ):
        """Test error when company has multiple integrations and no subdomain specified."""
        integration2 = MagicMock()
        integration2.subdomain = "testcompany2"

        with patch("services.integrations.ispcube.service.ISPCubeIntegration") as mock_model:
            # Mock the query chain properly with multiple integrations
            mock_query = MagicMock()
            mock_query.__iter__ = MagicMock(return_value=iter([mock_integration, integration2]))
            mock_model.objects.filter.return_value = mock_query

            with pytest.raises(ISPCubeError) as exc_info:
                get_company_ispcube_client(mock_company)

            assert "multiple ISPCube integrations" in str(exc_info.value)


class TestValidateISPCubeIntegration:
    """Tests for validate_ispcube_integration function."""

    @pytest.mark.asyncio
    async def test_successful_connection_test(self, mock_integration):
        """Test successful connection test."""
        with patch(
            "services.integrations.ispcube.service.get_ispcube_client"
        ) as mock_get_client:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.test_connection.return_value = True
            mock_get_client.return_value = mock_client

            success, error = await validate_ispcube_integration(mock_integration)

            assert success is True
            assert error is None

    @pytest.mark.asyncio
    async def test_failed_connection_test(self, mock_integration):
        """Test failed connection test."""
        with patch(
            "services.integrations.ispcube.service.get_ispcube_client"
        ) as mock_get_client:
            mock_client = AsyncMock()
            mock_client.__aenter__.return_value = mock_client
            mock_client.__aexit__.return_value = None
            mock_client.test_connection.return_value = False
            mock_get_client.return_value = mock_client

            success, error = await validate_ispcube_integration(mock_integration)

            assert success is False
            assert error == "Connection test failed"

    @pytest.mark.asyncio
    async def test_connection_test_with_exception(self, mock_integration):
        """Test connection test with exception."""
        with patch(
            "services.integrations.ispcube.service.get_ispcube_client"
        ) as mock_get_client:
            mock_client = AsyncMock()
            mock_client.__aenter__.side_effect = Exception("Network error")
            mock_get_client.return_value = mock_client

            success, error = await validate_ispcube_integration(mock_integration)

            assert success is False
            assert "Network error" in error

