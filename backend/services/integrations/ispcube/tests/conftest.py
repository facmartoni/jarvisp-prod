"""
Pytest configuration for ISPCube integration tests.
"""

import os
import django
import pytest

# Configure Django settings for tests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


@pytest.fixture(scope="session")
def anyio_backend():
    """Configure anyio backend for async tests."""
    return "asyncio"

