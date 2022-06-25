![example event parameter](https://github.com/Evgenia789/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)
# Проект - сайт Foodgram, «Продуктовый помощник»
 Проект Foodgram позволяет пользователем публиковать свои рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.d

## Техническое описание проекта Foodgram

К проекту по адресу http://127.0.0.1:8000/redoc/ подключена документация API Foodgram. В ней описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа: пользовательские роли, которым разрешён запрос.

## Cтек технологий

- проект написан на Python с использованием веб-фреймворка Django REST Framework.
- библиотека Djoser - авторизация пользователя
- библиотека django-filter - фильтрация запросов
- база данных - PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- настроено CI и CD для проекта (реализован автоматический запуск тестов, обновление образов на Docker Hub, автоматический деплой на боевой сервер при пуше в главную ветку main) 
- система управления версиями - git.

## Как запустить проект, используя Docker (база данных PostgreSQl):
Клонировать репозиторий и перейти в него в командной строке:
```bash
    git clone https://github.com/Evgenia789/foodgram-project-react
```
В дериктории проекта создайте файл .env, в котором пропишите следующие переменные окружения (для тестирования можете использовать указанные значения переменных):

- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=postgres
- POSTGRES_USER=admin
- POSTGRES_PASSWORD=987Bon321
- DB_HOST=db
- DB_PORT=5432

С помощью Dockerfile и docker-compose.yaml разверните проект:
```bash
    docker-compose up --build
```
В новом окне терминала узнайте id контейнера yamdb_web и войдите в контейнер:
```bash
    docker container ls
```
```bash
    docker exec -it <CONTAINER_ID> bash
```
В контейнере выполните миграции, создайте суперпользователя и заполните базу начальными данными:
```bash
    docker-compose exec backend python manage.py migrate
    docker-compose exec backendv python manage.py createsuperuser
    docker-compose exec backend python manage.py collectstatic --no-input
```
____
Ваш проект запустился на http://localhost/  
Полная документация (redoc.yaml) доступна по адресу http://localhost/redoc/  

## Алгоритм регистрации новых пользователей

1. Пользователь отправляет POST-запрос с параметрами email, username, first_name, last_name, password на эндпоинт /api/users/
2. Пользователь отправляет отдельный POST-запрос с параметрами email и password на эндпоинт /api/auth/token/login/, в ответе на запрос ему приходит token.

В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.

## Ресурсы Foodgram
- Ресурс auth: аутентификация.
- Ресурс users: пользователи.
- Ресурс recipes: рецепты пользователей.
- Ресурс ingredients: ингредиенты.
- Ресурс tags: тэги, к одному рецепту может быть привязано несколько тегов.
- Ресурс favorite: рецепты добавленные в список избранного определенного пользователя.
- Ресурс shopping_cart: рецепты добавленные в список покупок определенного пользователя.

## Пример http-запроса (POST) 
```
    url = 'http://localhost/api/recipes/{id}/favorite/' 
    data = {"id": 0,
            "name": "string",
            "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
            "cooking_time": 1}  
    headers = {'Authorization': 'Token your_token'}  
    request = request.post(url, data=data, headers=headers)  
```
## Ответ API_Foodgram:
```
Статус - код 201
{
"id": 0,
"name": "string",
"image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
"cooking_time": 1
```
```
Статус - код 400
{
"errors": "string"
}
```
```
Статус - код 401
{
"detail": "Учетные данные не были предоставлены."
}
```
