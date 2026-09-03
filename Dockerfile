FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY app ./app
COPY src ./src
COPY config.json ./

# Bounds match the web extra in pyproject.toml so a new release cannot change the image.
RUN pip install --no-cache-dir "fastapi>=0.115,<1" "uvicorn>=0.32,<1"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
