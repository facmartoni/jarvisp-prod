# Backend

Django backend with GraphQL API using service-oriented architecture.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Run migrations:
```bash
uv run python manage.py migrate
```

4. Create superuser:
```bash
uv run python manage.py createsuperuser
```

5. Start server:
```bash
uv run python manage.py runserver
```

## Architecture

### Service-Oriented Design
Instead of traditional Django MVC, this project uses services:

```
api/
  schema.py          # GraphQL schema and resolvers
services/
  example_service.py # Business logic
```

### Adding New Features

1. Create a service in `services/`:
```python
class UserService:
    @staticmethod
    def create_user(username: str, email: str):
        # Business logic here
        pass
```

2. Add GraphQL types and resolvers in `api/schema.py`:
```python
class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    
    def resolve_users(self, info):
        return UserService.get_all_users()
```

## Django Admin

Accessible at http://localhost:8000/admin/

Uses django-unfold for a modern admin interface.

## GraphQL Endpoint

- URL: http://localhost:8000/graphql/
- GraphiQL Interface: Enabled in development

## Environment Variables

See `.env.example` for required variables.