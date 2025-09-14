# Тестовый фреймворк для Restful Booker API

## Установка

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск тестов

1. Запустите тесты с Allure:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

2. Запуск линтеров:
   ```bash
   # Проверка стиля кода
   flake8 .
   
   # Форматирование кода
   black .
   
   # Сортировка импортов
   isort .
   
   # Проверка безопасности
   bandit -r .
   safety check
   ```

## CI/CD с GitHub Actions

Проект настроен для автоматического запуска тестов при каждом pull request. Настроены следующие workflow:

### 1. Основной CI Pipeline (`.github/workflows/ci.yml`)
- **Тестирование**: Запуск тестов на Python 3.8, 3.9, 3.10, 3.11
- **Линтинг**: Проверка кода с помощью flake8, black, isort
- **Безопасность**: Сканирование с bandit и safety
- **Артефакты**: Сохранение Allure отчетов

### 2. Allure Reports (`.github/workflows/allure-report.yml`)
- Генерация и публикация Allure отчетов на GitHub Pages
- Доступ к отчетам: `https://yourusername.github.io/yourrepo`

### Настройка GitHub репозитория

1. **Включите GitHub Pages**:
   - Перейдите в Settings → Pages
   - Выберите Source: GitHub Actions

2. **Настройте защиту веток**:
   - Settings → Branches → Add rule
   - Требуйте прохождения всех проверок CI
   - Требуйте обновления ветки перед merge

3. **Настройте CODEOWNERS** (опционально):
   - Обновите файл `.github/CODEOWNERS`
   - Укажите актуальных владельцев кода

### Локальная разработка

Для поддержания качества кода локально:

```bash
# Установка pre-commit hooks (рекомендуется)
pip install pre-commit
pre-commit install

# Запуск всех проверок локально
flake8 .
black --check .
isort --check-only .
bandit -r .
safety check
pytest
```

## Структура проекта

- `conftest.py` - фикстуры pytest
- `services/api_client.py` - класс для работы с API
- `utils/data_generator.py` - генерация данных через Faker
- `services/models/schemas.py` - Pydantic-схемы для валидации
- `tests/test_auth.py` - тесты аутентификации
- `tests/test_booking.py` - тесты бронирования
- `tests/test_ping.py` - тест проверки доступности API
- `.github/workflows/` - GitHub Actions workflows
- `.github/pull_request_template.md` - шаблон для PR 