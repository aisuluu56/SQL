# Практика 26 — PostgreSQL + Flet: хранение данных
# ЗАДАЧА: учёт кабинетов колледжа (не повторяет демонстрацию про заметки).
# Перед работой прочитайте lessons/26_postgresql.md и настройте .env.

"""Запускаемая заготовка: заполните TODO, чтобы подключить PostgreSQL."""
import os
from pathlib import Path

import flet as ft
import psycopg
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")


def open_connection():
    """Подключение для каждой короткой операции. Транзакция завершится при выходе из with."""
    if not DATABASE_URL:
        raise RuntimeError("Нет DATABASE_URL. Скопируйте .env.example в .env и настройте PostgreSQL")
    return psycopg.connect(DATABASE_URL, connect_timeout=5)


def initialize_db() -> None:
    # TODO: через with open_connection() as conn создайте таблицу rooms.
    # Поля: id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # number VARCHAR(20) NOT NULL UNIQUE, seats INTEGER NOT NULL CHECK (seats > 0).
    pass


def load_rooms() -> list[tuple[int, str, int]]:
    # TODO: подключитесь к БД, выполните SELECT id, number, seats FROM rooms ORDER BY id.
    # Верните список строк результата. Для этого используйте cur.fetchall().
    return []


def main(page: ft.Page) -> None:
    page.title = "Кабинеты колледжа — PostgreSQL"
    number = ft.TextField(label="Номер кабинета")
    seats = ft.TextField(label="Количество мест")
    listing = ft.Column(spacing=6)
    status = ft.Text()

    def refresh() -> None:
        try:
            records = load_rooms()
        except (psycopg.Error, RuntimeError) as exc:
            status.value = f"Не удалось прочитать данные: {exc}"
            records = []
        listing.controls = [ft.Text(f"#{rid}: каб. {room}, мест: {count}")
                            for rid, room, count in records]

    def add_room(e) -> None:
        # TODO: проверьте номер и число мест (целое > 0).
        # TODO: выполните INSERT с параметрами %s, затем вызовите refresh().
        # TODO: покажите ошибку для повторного номера и временного сбоя БД.
        # TODO: добавьте кнопку удаления каждого кабинета по id с SQL DELETE.
        pass

    try:
        initialize_db()
        refresh()
    except (psycopg.Error, RuntimeError) as exc:
        status.value = f"Нет соединения с PostgreSQL: {exc}"

    page.add(
        ft.Text("Учёт кабинетов", size=24, weight=ft.FontWeight.BOLD),
        number, seats, ft.Button("Добавить кабинет", on_click=add_room),
        status, listing,
    )


if __name__ == "__main__":
    ft.run(main)
