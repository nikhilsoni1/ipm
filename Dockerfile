FROM python:3.10.0
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]