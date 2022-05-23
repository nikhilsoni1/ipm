FROM python:3.10.0
ENV DATABASE_URI=postgresql://postgres:postgres@database/postgres
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
# Dummy commit after remote repo name change