# Encryption Setup

This project uses Fernet (symmetric encryption) to protect sensitive credentials in the database.

## Encrypted Fields

The following fields are automatically encrypted/decrypted:
- `ISPCubeIntegration.password`
- `ISPCubeIntegration.api_key`
- `ISPCubeIntegration.api_token`

## Setup

### 1. Generate Encryption Key

```bash
uv run python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'
```

### 2. Add to Environment Variables

Copy `.env.example` to `.env` and add your generated key:

```bash
cp .env.example .env
```

Edit `.env` and set:
```
ENCRYPTION_KEY=your-generated-key-here
```

### 3. Apply Migrations

```bash
uv run python manage.py migrate
```

## How It Works

### Custom Fields

- `EncryptedCharField`: CharField with automatic encryption
- `EncryptedTextField`: TextField with automatic encryption

### Usage

```python
from api.fields import EncryptedCharField

class MyModel(models.Model):
    secret_data = EncryptedCharField(max_length=500)
```

Data is:
- **Encrypted** when saving to database
- **Decrypted** when retrieving from database
- Transparent to application code

### Security

- Encryption key stored in environment variables (not in code)
- Uses Fernet (AES 128-bit in CBC mode with PKCS7 padding)
- Key rotation requires re-encrypting existing data
- Never commit `.env` file to version control

## Testing Encryption

```bash
uv run python manage.py shell
```

```python
from api.models import ISPCubeIntegration, Company

# Create test company
company = Company.objects.create(
    name="Test",
    slug="test",
    timezone="America/Argentina/Buenos_Aires"
)

# Create integration with credentials
integration = ISPCubeIntegration.objects.create(
    company=company,
    subdomain="test",
    username="user",
    password="secret_password",
    api_key="secret_key"
)

# Password is automatically decrypted
print(integration.password)  # "secret_password"

# But stored encrypted in DB
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT password FROM api_ispcubeintegration WHERE id = %s", [integration.id])
    print(cursor.fetchone()[0])  # "gAAAAAB..." (encrypted)
```

## Key Rotation

To rotate encryption keys:

1. Generate new key
2. Decrypt all data with old key
3. Re-encrypt with new key
4. Update `ENCRYPTION_KEY` in `.env`

**Note**: Key rotation script should be created before production use.

