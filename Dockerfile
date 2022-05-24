FROM python:3.10.0

# Environment Variables
ARG DATABASE_URI
ARG CSV_EXPORT_URI
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URI=${DATABASE_URI}
ENV CSV_EXPORT_URI=${CSV_EXPORT_URI}

# Build
COPY ./ /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/app
RUN alembic upgrade head
RUN python migrate_data.py
