# YAM — история чарта Яндекс Музыки

![Python](https://img.shields.io/badge/python-3.11-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)

Сервис собирает ежедневный чарт Яндекс Музыки (Россия, топ-100) и показывает, как менялись позиции треков во времени.

## Возможности

- **Сбор данных** — cron-задача (`django-crontab`) каждое утро получает чарт через неофициальный API Яндекс Музыки и сохраняет позиции всех треков. То же самое можно запустить вручную: `python manage.py get_chart`.
- **Чарт на дату** — `/chart/?date=2024-09-08` показывает чарт за выбранный день.
- **Динамика трека** — `/chart/?track=<название>` находит трек через поиск Яндекс Музыки и строит график его позиций по дням (matplotlib, встраивается в страницу как PNG).

## Стек

Django, PostgreSQL, `yandex-music`, matplotlib, cron, nginx, Docker Compose.

## Запуск

```bash
cp .env.template .env   # YANDEX_TOKEN, DATABASE_URL, DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS
docker compose up --build
```

Приложение будет доступно на http://localhost:8877/chart/. При старте контейнер применяет миграции, собирает статику и регистрирует cron-задачу. Чтобы не ждать утра, первый чарт можно загрузить сразу:

```bash
docker compose exec web python manage.py get_chart
```
