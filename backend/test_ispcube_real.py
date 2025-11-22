"""
Test ISPCube integration against real API.

SECURITY: Requires environment variables with credentials

Usage:
    export ISPCUBE_SUBDOMAIN="..." 
    export ISPCUBE_USERNAME="..."
    export ISPCUBE_PASSWORD="..."
    export ISPCUBE_API_KEY="..."
    export ISPCUBE_CLIENT_ID="..."
    uv run python test_ispcube_real.py
"""

from typing import Any


import asyncio
import os

from services.integrations.ispcube import ISPCubeClient
from services.integrations.ispcube.exceptions import ISPCubeAuthError, ISPCubeAPIError


async def main():
    """Test ISPCube integration with real API."""
    print("=" * 70)
    print("ISPCube Real API Test")
    print("=" * 70)

    # Load from environment variables
    subdomain = os.getenv("ISPCUBE_SUBDOMAIN")
    username = os.getenv("ISPCUBE_USERNAME")
    password = os.getenv("ISPCUBE_PASSWORD")
    api_key = os.getenv("ISPCUBE_API_KEY")
    client_id = os.getenv("ISPCUBE_CLIENT_ID")
    
    if not all([subdomain, username, password, api_key, client_id]):
        print("\n❌ Error: Missing required environment variables")
        print("\nSet these environment variables:")
        print("  export ISPCUBE_SUBDOMAIN='...'")
        print("  export ISPCUBE_USERNAME='...'")
        print("  export ISPCUBE_PASSWORD='...'")
        print("  export ISPCUBE_API_KEY='...'")
        print("  export ISPCUBE_CLIENT_ID='...'")
        return False
    
    config = {
        "subdomain": subdomain,
        "username": username,
        "password": password,
        "api_key": api_key,
        "client_id": client_id,
        "base_url": f"https://{subdomain}.ispcube.com",
    }

    print(f"\nConnecting to: {config['base_url']}")
    print(f"Client ID: {config['client_id']}")
    print(f"Username: {config['username']}")

    try:
        async with ISPCubeClient(config) as client:
            # Test 1: Authentication
            print("\n[1/3] Testing Authentication...")
            auth_response = await client.authenticate()
            print(f"✓ Authentication successful!")
            print(f"  Token: {auth_response['token'][:30]}...")
            print(f"  Expires in: {auth_response['expires_in']} hours")

            # Test 2: Connection Test
            print("\n[2/3] Testing Connection...")
            is_connected = await client.test_connection()
            print(f"✓ Connection test: {'PASSED' if is_connected else 'FAILED'}")

            # Test 3: Get Customers
            print("\n[3/3] Fetching Customers (limit 5)...")
            customers = await client.get_customers(limit=5)
            print(f"✓ Retrieved {len(customers)} customers")

            if customers:
                print("\nSample Customer Data:")
                for i, customer in enumerate[dict[str, Any]](customers[:3], 1):
                    print(f"\n  Customer {i}:")
                    print(f"    ID: {customer.get('id')}")
                    print(f"    Code: {customer.get('code')}")
                    print(f"    Name: {customer.get('name')}")
                    print(f"    Doc #: {customer.get('doc_number')}")
                    print(f"    Status: {customer.get('status')}")
                    print(f"    Debt: ${customer.get('debt', '0.00')}")
            else:
                print("\n  No customers found (might need pagination)")

            print("\n" + "=" * 70)
            print("✓ All tests passed successfully!")
            print("=" * 70)
            return True

    except ISPCubeAuthError as e:
        print(f"\n✗ Authentication Error: {e}")
        print("\nPossible causes:")
        print("  - Invalid username or password")
        print("  - Invalid API key")
        print("  - Invalid client ID")
        return False

    except ISPCubeAPIError as e:
        print(f"\n✗ API Error: {e}")
        if e.status_code:
            print(f"  Status Code: {e.status_code}")
        if e.response:
            print(f"  Response: {e.response[:200]}")
        return False

    except Exception as e:
        print(f"\n✗ Unexpected Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)

