# Приложение для оплаты товаров через stripeAPI
 Сервер со страницей информации о товаре и простой формой оплаты через stripeAPI
## Установка
1. Скопировать репозиторий <br>
```
git clone https://github.com/KaiReytsu/django_stripe_paymentAPI.git 
```
2. Переименовать `.env.example` в `.env` указав свои параметры, <br>
   а так же добавить публичный ключ stripe в файле static/script.js
```
mv .env.example .env
```
3. Установить [docker-compose](https://docs.docker.com/compose/install/#install-compose)
## Запуск
Для запуска сайта выполните команду
```
docker compose up
```
## Зависимости
Для разработки используется модуль [pipenv](https://pipenv.pypa.io/en/latest/). <br>
Для установки зависимостей выполните команду
```
pipenv install
```
___________________________________
Сервис развурнут на [https://djangostripeapi.space/item/1](https://djangostripeapi.space/item/1)
