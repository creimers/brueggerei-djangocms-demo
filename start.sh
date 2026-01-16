#!/bin/sh
set -e

(
    uv run python manage.py migrate --noinput
    uv run python manage.py collectstatic --noinput
) &

uv run uvicorn website.asgi:application --host 0.0.0.0 --port 8000
