FROM python:3.10.0-slim-buster
COPY ./ /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
