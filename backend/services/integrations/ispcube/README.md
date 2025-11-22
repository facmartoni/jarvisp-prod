# ISPCube Integration

Integration with ISPCube API - LATAM ISP management system.

**Status**: ✅ Tested with real API  
**Tests**: 26/26 passing  
**Docs**: https://apidoc.ispcube.com/  
**Security**: ⚠️ NEVER commit credentials - use environment variables

## Usage

```python
from services.integrations.ispcube import ISPCubeClient

config = {
    "subdomain": "myisp",           # From your ISPCube URL
    "username": "api",              # From ISPCube staff
    "password": "your-password",    # From ISPCube staff
    "api_key": "your-api-key-uuid", # From ISPCube staff
    "client_id": "123",             # Your company ID in ISPCube
    "base_url": "https://myisp.ispcube.com"
}

async with ISPCubeClient(config) as client:
    await client.authenticate()
    customers = await client.get_customers(limit=50)
```

### With Django

```python
from services.integrations.ispcube.service import get_company_ispcube_client

async with get_company_ispcube_client(company) as client:
    await client.authenticate()
    customers = await client.get_customers()
```

## Methods

- `authenticate()` - Get 24-hour token
- `test_connection()` - Verify connectivity
- `get_customers(**filters)` - List customers (supports: limit, offset, doc_number, deleted, temporary)

## Configuration

All credentials from ISPCube staff:

| Field | Example | Notes |
|-------|---------|-------|
| `subdomain` | `"myisp"` | From URL: https://myisp.ispcube.com |
| `client_id` | `"123"` | Your company ID in ISPCube |
| `api_key` | `"uuid-here"` | Static API key (UUID format) |
| `username` | `"api"` | API user |
| `password` | `"secret"` | API password |

## Testing

```bash
cd backend

# Unit tests (no credentials needed)
uv run pytest services/integrations/ispcube/tests/ -v --no-cov

# Real API test (requires environment variables)
export ISPCUBE_SUBDOMAIN="..."
export ISPCUBE_USERNAME="..."
export ISPCUBE_PASSWORD="..."
export ISPCUBE_API_KEY="..."
export ISPCUBE_CLIENT_ID="..."
uv run python test_ispcube_real.py
```

## Next Endpoints

Billing, tickets, connections, plans, nodes, cash operations
