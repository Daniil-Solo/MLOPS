# Проект  для курса MLOps

## Методология ведения репозитория

Методология ведения репозитория соответствует **Data Science Lifecycle Process**,
информация о которой доступна по [ссылке](https://github.com/dslp/dslp)

Назначения веток:
- master - основная ветка
- data/[issue-number]-* - ветка для изменения data pipeline
- experiment/[issue-number]-* - ветка для проведения исследования нового подхода/модели
- model/[issue-number] - ветка для приведения модели к production-виду на основе удачного эксперимента
- [issue-number]-* - для всего остального


## Окружения

### Окружение для разработки

#### Сборка
```bash
docker build -f Dockerfile.dev -t mlops-course/dev:latest .
```
#### Запуск
```bash
docker run --rm --name mlops-dev -p 8888:8888 --mount type=bind,source="$(pwd)"/notebooks/,target=/app/notebooks/ mlops-course/dev:latest
```
#### Остановка окружения
```bash
docker stop mlops-dev
```

### Окружение для продакшена

#### Сборка
```bash
docker build -f Dockerfile.prod -t mlops-course/prod:latest .
```
#### Запуск
```bash
docker run --rm --name mlops-prod mlops-course/prod:latest
```
#### Остановка окружения
```bash
docker stop mlops-prod
```