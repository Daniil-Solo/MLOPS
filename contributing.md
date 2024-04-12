# Участие в проекте

## Используемые линтеры

В проекте используется линтер/форматтер ruff и статический анализатор типов mypy.
Для удобства есть pre-commit-hook, запускающий необходимые проверки при коммите изменений

### Основные команды

#### Установка зависимостей
```bash
pip install poetry 
poetry install
```

#### Установка pre-commit и запуск проверок
```bash
pre-commit install
pre-commit run --all-files
```

#### Ручной запуск проверок
```bash
poetry run ruff check my_code.py
poetry run mypy my_code.py
```
