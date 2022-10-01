# API для Yatube

## Описание

Проект социальной сети, в которой реализованы возможности пользователю публиковать и редактировать свои записи, комментировать записи, подписываться на других авторов и отписываться от них.

## Установка

- Клонировать репозиторий и перейти в него в командной строке.
- Cоздать и активировать виртуальное окружение:
```python -m venv venv ```
```source venv/scripts/activate```
- Установить зависимости из файла requirements.txt:
```python -m pip install --upgrade pip```
```pip install -r requirements.txt```
- Выполнить миграции:
```python manage.py migrate```
- Запустить проект:
```python manage.py runserver```

## Примеры запросов
- Получить список всех публикаций:
```GET /api/v1/posts/```
- Создать публикацию:
```POST /api/v1/posts/```
- Получение публикации по id:
```GET /api/v1/posts/{id}/```
- Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены:
```PUT /api/v1/posts/{id}/```
- Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены:
```PATCH /api/v1/posts/{id}/```
- Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены:
```DELETE /api/v1/posts/{id}/```
- Получение всех комментариев к публикации:
```GET /api/v1/posts/{post_id}/comments/```

## Технологии

- Python 3.7
- Django 2.2
- Django REST Framework
- JWT
- Djoser


### Автор
Наташа Сорокина =)