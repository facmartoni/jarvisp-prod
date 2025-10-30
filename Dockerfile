FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files from backend directory
COPY backend/pyproject.toml backend/uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code from backend directory
COPY backend/ .

# Collect static files
RUN uv run python manage.py collectstatic --noinput

# Expose port
EXPOSE 8080

# Start server
CMD uv run gunicorn config.wsgi:application --bind 0.0.0.0:8080 --workers 2

