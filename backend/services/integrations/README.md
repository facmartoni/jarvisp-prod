# ISP Integrations

Integrations with LATAM ISP management systems for Macch AI assistant.

## ISPCube ✅

**Status**: Auth + customers working (tested with real API)  
**Tests**: 26/26 passing

```python
from services.integrations.ispcube import ISPCubeClient

config = {
    "subdomain": "myisp",  
    "username": "api",
    "password": "your-password",  # All from ISPCube staff
    "api_key": "your-api-key",
    "client_id": "123",
    "base_url": "https://myisp.ispcube.com"
}

async with ISPCubeClient(config) as client:
    await client.authenticate()
    customers = await client.get_customers()
```

See `ispcube/README.md` for details.

## Architecture

- **Base class**: Only requires `authenticate()` and `test_connection()`
- **System-specific methods**: ISPCube has `get_customers()`, SmartOLT will have `get_olts()`, etc.
- **Async, type-safe, Django helpers**

## Testing

```bash
cd backend
uv run pytest services/integrations/ispcube/tests/ --no-cov -q  # Unit tests
```

## Adding Integrations

1. Inherit `BaseISPIntegration`
2. Implement `authenticate()` + `test_connection()`
3. Add system-specific methods
4. Write tests

Structure: `newsystem/client.py`, `exceptions.py`, `types.py`, `service.py`, `tests/`

## Planned

- SmartOLT (network devices)
- Gestión Real (full ISP management)
- MikroWISP (wireless)
