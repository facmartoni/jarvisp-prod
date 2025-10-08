# Jarvis P

Full-stack application with Django backend and React frontend, communicating via GraphQL.

## Tech Stack

### Backend
- **Python**: 3.13.3
- **Django**: 5.2.7
- **GraphQL**: Graphene-Django 3.2.3
- **Package Manager**: uv 0.7.10

### Frontend
- **React**: 19.2.0
- **TypeScript**: 5.9.3
- **Vite**: 7.1.9
- **Apollo Client**: 4.0.7
- **Package Manager**: pnpm 10.11.0

## Project Structure

```
jarvisp/
├── backend/          # Django backend with service-oriented architecture
│   ├── api/          # GraphQL schema and resolvers
│   ├── services/     # Business logic layer
│   └── config/       # Django configuration
└── frontend/         # React + TypeScript frontend
    └── src/          # Frontend source code
```

## Getting Started

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Run migrations:
```bash
uv run python manage.py migrate
```

4. Create superuser (optional):
```bash
uv run python manage.py createsuperuser
```

5. Start development server:
```bash
uv run python manage.py runserver 8001
```

Backend will be available at: http://localhost:8001
- GraphQL endpoint: http://localhost:8001/graphql/
- Admin panel: http://localhost:8001/admin/

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Start development server:
```bash
pnpm dev
```

Frontend will be available at: http://localhost:5173

## Architecture

### Backend (Service-Oriented)
The backend follows a service-oriented architecture instead of traditional MVC:
- **Services**: Business logic encapsulation (`backend/services/`)
- **API Layer**: GraphQL resolvers that call services (`backend/api/`)
- **Models**: Database models (when needed)

### Frontend
- Component-based React architecture
- Apollo Client for GraphQL state management
- TypeScript for type safety

## Development

### Running Both Servers

Terminal 1 (Backend):
```bash
cd backend && uv run python manage.py runserver 8001
```

Terminal 2 (Frontend):
```bash
cd frontend && pnpm dev
```

### Testing GraphQL

Visit http://localhost:8001/graphql/ to use GraphiQL interface.

Example query:
```graphql
{
  hello
}
```
