# Настройка проекта

Все команды для Windows

>git clone https://github.com/spurdo-B3/backend.git - клонирование проекта

>python -m venv venv - создание виртуального окружения

>venv/Scripts/activate - активация виртуального окружения

>pip install -r req.txt - установка зависимостей

>cd app - переходим в папку app

Не забываем настроить .env, пример файла находится в .env.example

>python manage.py collectstatic - для nginx

>python manage.py runserver - запуск сервера django

## Команды по docker

> docker compose up --build - запуск docker контейнера

> docker compose exec -it backend-django /bin/sh - проваливаемся в файловую систему docker'a

> docker compose down - сбросить контейнер
 
> docker compose down --volumes - сбросить контейнеры с волюмами (в редких случаях)
