# Практика 28 — Итоговый проект: система заявок на ремонт ПК
# ЗАДАЧА: сервис-деск колледжа с Flet и PostgreSQL.
# Перед началом: lessons/28_capstone.md и db/README.md.
# TODO помечает операции, которые предстоит реализовать самостоятельно.

"""Стартовый каркас: UI запускается, а SQL/CRUD и маршруты дописывает студент."""
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path

import flet as ft
import psycopg
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")
STATUSES = ("Новая", "В работе", "Закрыта")


@dataclass
class Ticket:
    id: int
    title: str
    room: str
    status: str = "Новая"
    created_at: datetime | None = None


def open_connection():
    if not DATABASE_URL:
        raise RuntimeError("Настройте DATABASE_URL в файле .env (см. db/README.md)")
    return psycopg.connect(DATABASE_URL, connect_timeout=5)


def initialize_db() -> None:
    # TODO: создайте таблицу tickets в PostgreSQL:
    # id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # title TEXT NOT NULL, room VARCHAR(20) NOT NULL,
    # status TEXT NOT NULL DEFAULT 'Новая', created_at TIMESTAMPTZ DEFAULT now().
    # Добавьте CHECK, ограничивающий возможные значения status.
    pass


def load_tickets() -> list[Ticket]:
    # TODO: SELECT id, title, room, status, created_at FROM tickets ORDER BY id.
    # Преобразуйте строки из cur.fetchall() в список объектов Ticket.
    return []


def insert_ticket(title: str, room: str) -> int | None:
    # TODO: INSERT ... VALUES (%s, %s) RETURNING id.
    # Верните созданный id; если нужна проверка полей, выполните её до INSERT.
    return None


def update_ticket_status(ticket_id: int, new_status: str) -> None:
    # TODO: UPDATE ... WHERE id = %s; проверьте значение new_status.
    pass


def delete_ticket(ticket_id: int) -> None:
    # TODO: DELETE ... WHERE id = %s; покажите подтверждение в UI.
    pass


def main(page: ft.Page) -> None:
    page.title = "Сервис-деск колледжа — PostgreSQL"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
    error = ft.Text()
    tickets: list[Ticket] = []
    try:
        initialize_db()
        tickets = load_tickets()
    except (psycopg.Error, RuntimeError) as exc:
        error.value = f"Нет доступа к PostgreSQL: {exc}"

    title = ft.TextField(label="Описание проблемы")
    room = ft.TextField(label="Кабинет")
    search = ft.TextField(label="Поиск")
    listing = ft.Column(spacing=8)
    info = ft.Text()

    def render(e=None) -> None:
        # TODO: добавьте поиск, фильтр статуса, сортировку и пустое состояние.
        # TODO: кнопки перехода к деталям и удаления с подтверждением.
        listing.controls = [
            ft.Card(content=ft.Container(padding=10,
                content=ft.Text(f"#{ticket.id} {ticket.title} — {ticket.status}")))
            for ticket in tickets
        ]
        info.value = f"Всего заявок: {len(tickets)}"

    def create_ticket(e) -> None:
        # TODO: проверьте форму, вызовите insert_ticket(title.value, room.value),
        # перечитайте записи из PostgreSQL и перерисуйте список.
        # Не храните изменения только в локальном списке tickets.
        pass

    search.on_change = render
    render()
    page.add(ft.Column(controls=[
        ft.Text("Заявки", size=28, weight=ft.FontWeight.BOLD),
        error, title, room,
        ft.Button("Новая заявка", on_click=create_ticket),
        search, info, listing,
    ], scroll=ft.ScrollMode.AUTO))
    # TODO: добавьте View для списка, формы и деталей; реализуйте редактирование статуса.


if __name__ == "__main__":
    ft.run(main)
