FROM python:3.10.0
COPY ./ /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt