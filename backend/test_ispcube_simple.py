"""
Simple ISPCube integration test.

SECURITY: Requires environment variables with credentials

Usage:
    export ISPCUBE_SUBDOMAIN="..." 
    export ISPCUBE_USERNAME="..."
    export ISPCUBE_PASSWORD="..."
    export ISPCUBE_API_KEY="..."
    export ISPCUBE_CLIENT_ID="..."
    uv run python test_ispcube_simple.py
"""

import asyncio
import os

from services.integrations.ispcube import ISPCubeClient


async def test_ispcube():
    """Simple test with credentials from environment or ispcubecreds.txt."""
    
    # Load from environment variables (NEVER hardcode credentials)
    subdomain = os.getenv("ISPCUBE_SUBDOMAIN")
    username = os.getenv("ISPCUBE_USERNAME")
    password = os.getenv("ISPCUBE_PASSWORD")
    api_key = os.getenv("ISPCUBE_API_KEY")
    client_id = os.getenv("ISPCUBE_CLIENT_ID")
    
    if not all([subdomain, username, password, api_key, client_id]):
        print("Error: Set environment variables:")
        print("  ISPCUBE_SUBDOMAIN, ISPCUBE_USERNAME, ISPCUBE_PASSWORD,")
        print("  ISPCUBE_API_KEY, ISPCUBE_CLIENT_ID")
        return
    
    config = {
        "subdomain": subdomain,
        "username": username,
        "password": password,
        "api_key": api_key,
        "client_id": client_id,
        "base_url": f"https://{subdomain}.ispcube.com",
    }
    
    print("Testing ISPCube integration...")
    
    async with ISPCubeClient(config) as client:
        # Authenticate
        await client.authenticate()
        print("✓ Authenticated")
        
        # Get customers
        customers = await client.get_customers(limit=3)
        print(f"✓ Retrieved {len(customers)} customers")
        
        for customer in customers:
            print(f"  - {customer['name']} ({customer['code']})")
    
    print("✓ Test complete")


if __name__ == "__main__":
    asyncio.run(test_ispcube())

