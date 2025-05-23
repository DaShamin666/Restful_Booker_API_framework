# Тестовый фреймворк для Restful Booker API

## Установка

1. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Запуск тестов

1. Запустите тесты с Allure:
   ```
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

## Структура проекта

- `conftest.py` - фикстуры pytest
- `utils/api_client.py` - класс для работы с API
- `utils/data_generator.py` - генерация данных через Faker
- `utils/schemas.py` - Pydantic-схемы для валидации
- `tests/test_auth.py` - тесты аутентификации
- `tests/test_booking.py` - тесты бронирования
- `tests/test_ping.py` - тест проверки доступности API 