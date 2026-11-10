# Подготовка PostgreSQL для практик 26 и 28

Курс использует **PostgreSQL + Psycopg 3**, без SQLite. Весь учебник (темы 1–25 и 27) можно изучать и без сервера, однако задания 26 и 28 требуют работающей БД.

## Вариант А. Через Docker Compose

1. Установите Docker Desktop, если он ещё не установлен.
2. В корне курса скопируйте `.env.example` → `.env`.
3. В `.env` замените `replace_with_local_password` на **свой учебный пароль в обоих местах** (`POSTGRES_PASSWORD` и `DATABASE_URL`). Для начала используйте пароль без `@`, `:`, `/`, `#` и пробелов; эти символы потребуют URL-кодирования.
4. Выполните в корне курса:

```bash
docker compose up -d
docker compose ps
```

Сервер будет доступен на `localhost:5433`; имя БД — `flet_academy`, пользователь — `flet_student`. Данные PostgreSQL хранятся в Docker-томе и не пропадают после остановки контейнера.

Команды для проверки сервера и подключения к SQL-терминалу:

```bash
docker compose exec postgres pg_isready -U flet_student -d flet_academy
docker compose exec postgres psql -U flet_student -d flet_academy
```

В `psql` проверьте `SELECT current_database();`, затем выйдите через `\q`. Остановка без удаления тома: `docker compose down`. Команда `docker compose down -v` **удаляет учебную базу и все сохранённые в томе данные** — не выполняйте её, если хотите сохранить результаты.

## Вариант Б. Уже установлен PostgreSQL

1. Создайте отдельную учебную базу `flet_academy` и пользователя с разрешениями на создание таблиц (через pgAdmin/psql).
2. Скопируйте `.env.example` → `.env`.
3. Укажите в `DATABASE_URL` имя пользователя, пароль, хост, **реальный порт** PostgreSQL (часто `5432`) и название базы. Docker при этом не нужен.
4. Проверьте соединение:

```bash
python -c "from dotenv import load_dotenv; load_dotenv(); import os, psycopg; conn=psycopg.connect(os.environ['DATABASE_URL']); print('PostgreSQL подключён'); conn.close()"
```

## Заметки

- В `.env` находятся пароли: **не отправляйте этот файл студентам с настоящими учётными данными и не коммитьте в Git**. В комплект входит только `.env.example` с вымышленным паролем.
- Не делайте `DROP DATABASE` / `DROP TABLE` ради перезапуска темы: кнопка «Сбросить тему» в тренажёре сбрасывает **только отметки прогресса**, не записи PostgreSQL.
- Если сменить `POSTGRES_PASSWORD` в `.env` после первого создания тома, PostgreSQL не поменяет пароль существующего пользователя автоматически. Поменяйте пароль через SQL `ALTER ROLE` или используйте новый учебный том, если старые данные не нужны.
- Подключение к Docker-PostgreSQL ограничено интерфейсом `127.0.0.1`; учебные пароли не предназначены для публичного сервера.
