# Сервис для бронирования переговорных

- [ ] [Описание](#описание)
- [ ] [Технологии](#технологии)
- [ ] [Начало работы](#начало-работы)
- [ ] [Зависимости](#зависимости)
- [ ] [Установка](#установка)
- [ ] [Использование API сервиса до развертки](#использование-api-сервиса-до-развертки)
 

### Описание
Сервис для бронирования переговорных реализован на асинхронном фреймворке FastAPI.
API полностью дают возможность реализовать полноценный web-сервис для бронирования переговорных у вас в компании с поддержкой администратора и обычными пользователями. 

### Технологии
[![Python][Python-badge]][Python-url] [![FastAPI][FastAPI-badge]][FastAPI-url] [![PostgreSQL][PostgreSQL-badge]][PostgreSQL-url]

### Начало работы

Чтобы запустить локальную копию сервиса, следуй инструкциям ниже.

### Зависимости

- [Python 3.7+][Python-url]

### Установка

1. **Клонировать репозиторий**

    ```shell
    git clone git@github.com:reztsovdimitrii/booking_meeting_room.git
    ```
2. **Создать, активировать виртуальное окружение**
	```shell
    python -m venv venv
    ```
3. **Установить зависимости проекта**
    ```shell
    pip install -r requirements.txt
    ```
4. **Создание базы данных и переменного окружения**
	Сервис использует базу данных PostgreSQL, поэтому нужно установить себе на локальный сервер.  
	Для подключения и выполнения запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корневой папке сервиса.

	Шаблон для заполнения файла ".env":
	```python
	APP_TITLE=Сервис бронирования переговорных комнат # тут вы можете назвать свой API
	APP_DESCRIPTION=API сервиса бронирования переговорных комнат с пользователями и администраторами. # тут описание API
	DATABASE_URL=postgresql+asyncpg://{user}:{password}@{localgost}:{port}/{name_db} # ссылка на подключение к вашей БД, обратите внимание на драйвер подключения asyncpg к БД
	SECRET={example} # любой на ваше усмотрение ENG
	FIRST_SUPERUSER_EMAIL=admin@admin.com
	FIRST_SUPERUSER_PASSWORD=admin
	```
5.  **Создать базу данных и выполнить миграции**
	В терминале bash корневой директории сервиса booking_meeting_room запустить команду для миграции базы данных. Перед этим убедится, что ваша БД развернута и активна.
	```bash
	alembic upgrade head
	```
6. **Запуск API сервиса для бронирования переговорных**
	Запустить сервис можно в терминале bash командой:
	```bash
	uvicorn app.main:app --reload
	```
	После запуска сервиса автоматически будет создан администратор. Доступ к API сервиса можно проверить по адресу [http://localhost/docs](http://localhost:8000/docs) будет запущена открытая документация API формата Swagger, где вы можете войти под администратором и выполнить запросы на эндпоинты.

### Использование API сервиса до развертки
В корневой директории проекта находится redoc.json с помощью сервиса [Redocly](https://redocly.github.io/redoc/) можно прочитать как устроен данный API до запуска сервиса на локальном сервере. Если вас устроит данный web-сервис буду рад помочь =)

---

<h4 align="center">
Автор сервиса: <a href="https://github.com/reztsovdimitrii">Дмитрий Резцов</a>
</h4>

<!-- MARKDOWN BADGES & URLs -->

[Python-url]: https://www.python.org/
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[FastAPI-url]: https://fastapi.tiangolo.com/
[FastAPI-badge]: https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[PostgreSQL-badge]: https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white