FROM python:3.10.0-slim-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt