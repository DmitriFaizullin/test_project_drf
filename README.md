# <p style="text-align:center">API интернет-магазина</p>
***
### Описание проекта.

Проект API интернет-магазина с системой аутентификации, управления товарами и корзиной покупок.
Выполнен в соответствии с тестовым заданием на позицию стажера python backend development.
В проекте предусмотрена возможность аутентификации и авторизации черерз Djoser. Управление
товарами предусматривает просмотр списка товаров с детальной информацией. Управление корзиной покупок
позволяет осуществлять добавление товаров (только для аутентифицированных пользователей),
просмотр корзины с подсчетом общей суммы и количества товаров, обновлене количества товаров, удаление
товаров из корзины, очистка корзины. Реализована возможность управления с использованием
административной панели. Проект содержит автоматически сгенерированную документацию Swagger.
***
### Использованные технологии.
Backend: Django 3.2
- API: Django REST Framework 3.12
- Аутентификация: Djoser, Token Authentication
- База данных: SQLite
- Административная панель: Django Admin
***
### Запуск приложения локально.
1. Предварительные требования для запуска проекта
Python 3.8+
pip (менеджер пакетов Python)

2. Клонирование репозитория
```git clone git@github.com:DmitriFaizullin/test_project_drf.git```
```cd test_project_drf/```

3. Создание виртуального окружения
```python -m venv venv```
```source venv/bin/activate  # Linux/MacOS```
или
```venv\Scripts\activate  # Windows```

4. Установка зависимостей
```pip install -r requirements.txt```


5. Настройка базы данных
```cd test_project_drf/```
```python manage.py migrate```

6. Загрузка тестовых данных
```python manage.py load_fixtures```

7. Создание суперпользователя (опционально)
```python manage.py createsuperuser```

 8. Запуск сервера разработки
```python manage.py runserver```

Приложение будет доступно по адресу: http://localhost:8000

Документация доступна по адресу: http://localhost:8000/docs

Административная панель доступна по адресу: http://localhost:8000/admin
***
### Эндпоинты API.
Публичные эндпоинты (не требуют аутентификации)
- GET /api/products/ - список товаров
- GET /api/products/{id}/ - детали товара
- GET /api/categories/ - список категорий

Защищенные эндпоинты (требуют аутентификации)
- GET /api/cart/ - просмотр корзины
- POST /api/cart/ - добавление товара в корзину
- PUT/PATCH /api/cart/{id}/ - обновление количества товара
- DELETE /api/cart/{id}/ - удаление товара из корзины
- DELETE /api/cart/clear/ - очистка всей корзины

Аутентификация
- POST /api/users/ - регистрация пользователя
- POST /api/token/login/ - получение токена
- POST /api/token/logout/ - выход из системы
***
### Примеры использования.
Добавление товара в корзину
```
curl -X POST http://localhost:8000/cart/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"product": 1, "quantity": 2}'
```
Просмотр корзины
```
curl -X GET http://localhost:8000/cart/ \
  -H "Authorization: Token <your-token>"
```
Очистка корзины
```
curl -X DELETE http://localhost:8000/cart/clear/ \
  -H "Authorization: Token <your-token>"
```

***
Тестовый проект выполнил
Файзуллин Дмитрий Андреевич
Ссылка на страницу [GitHub](https://github.com/DmitriFaizullin/).
