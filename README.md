![example event parameter](https://github.com/Evgenia789/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)
# Сайт Foodgram, «Продуктовый помощник»
 Проект Foodgram позволяет пользователем публиковать свои рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Cтек технологий

- проект написан на Python3.7 с использованием веб-фреймворка Django REST Framework.
- библиотека Djoser - авторизация пользователя
- библиотека django-filter - фильтрация запросов
- база данных - PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- настроено CI и CD для проекта (реализован автоматический запуск тестов, обновление образов на Docker Hub, автоматический деплой на боевой сервер при пуше в главную ветку main) 
- система управления версиями - git

## Как запустить проект, используя Docker (база данных PostgreSQl):
Клонировать репозиторий и перейти в него в командной строке:
```bash
    git clone https://github.com/Evgenia789/foodgram-project-react
    cd foodgram-project-react
```
Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
В дериктории проекта создайте файл .env, в котором пропишите следующие переменные окружения (SECRET_KEY нужно взять из settings.py):
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=654qwe345
DB_HOST=db
DB_PORT=5432
DEBUGE=TRUE
SECRET_KEY=<SECRET_KEY>
```

Соберите контейнеры:
```bash
    docker-compose up -d --build 
```
Выполните по очереди команды:
```bash
    docker-compose exec backend python manage.py makemigrations
    docker-compose exec backend python manage.py migrate
    docker-compose exec backend python manage.py add_ingredients
    docker-compose exec backend python manage.py createsuperuser
    docker-compose exec backend python manage.py collectstatic --no-input 
```
____
Ваш проект запустился на http://localhost/
