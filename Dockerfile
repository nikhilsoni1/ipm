FROM python:3.10.0
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV DATABASE_URI=postgresql://postgres:postgres@database/postgres
WORKDIR /app/pincode_service/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]