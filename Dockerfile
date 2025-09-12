# Используем образ Python
FROM python:3.9-slim

LABEL authors="a123"

# Установка необходимых библиотек
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все необходимые файлы в контейнер
COPY ./tests /app/tests
COPY ./services /app/services
COPY ./utils /app/utils
COPY conftest.py /app/conftest.py

# Установим PYTHONPATH для корректного импорта модулей
ENV PYTHONPATH=/app

# Команда для запуска тестов
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q", "tests/"]
