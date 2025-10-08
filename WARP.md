# JarvISP - Warp Project Configuration

Full-Stack Python Django + React TypeScript + GraphQL application.

## Tech Stack

### Backend
- Python, Django, GraphQL (Graphene-Django)
- Package manager: `uv`

### Frontend
- React, TypeScript, Vite, Apollo Client
- Package manager: `pnpm`

## Architecture

### Backend (Service-Oriented)
- Services: `backend/services/` - Business logic
- API: `backend/api/` - GraphQL resolvers
- Admin: django-unfold at http://localhost:8001/admin/

### Frontend
- Component-based React with Apollo Client
- GraphQL state management

## Development Commands

### Backend
- Django commands: `uv run python manage.py [command]`
- Migrations: `uv run python manage.py migrate`
- Create superuser: `uv run python manage.py createsuperuser`

### Frontend
- Dev server: `pnpm dev`
- Build: `pnpm build`
- Lint: `pnpm lint`

## Project Structure
```
jarvisp/
├── backend/          # Django + GraphQL
│   ├── api/          # Schema and resolvers
│   ├── services/     # Business logic
│   └── config/       # Django config
└── frontend/         # React + TypeScript
    └── src/          # Source code
```
