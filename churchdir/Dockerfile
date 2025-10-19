# Simple production-ish container
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     DJANGO_SETTINGS_MODULE=churchdir.settings

WORKDIR /app

# System deps (psycopg2 can be added later if switching to Postgres)
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# collect static (noop for now, but fine)
RUN python manage.py collectstatic --noinput || true

# Default: gunicorn on 0.0.0.0:8000
EXPOSE 8000
CMD ["gunicorn", "churchdir.wsgi:application", "--bind", "0.0.0.0:8000"]
