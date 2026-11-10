# Практика 23 — Повторно используемые UI-компоненты
# ЗАДАЧА: Переиспользуемая карточка заявки
# Откройте соответствующий lessons/23_reuse.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

TICKETS = [
    {"id": 1, "title": "Не включается ПК", "status": "Новая"},
    {"id": 2, "title": "Нет сети", "status": "В работе"},
    {"id": 3, "title": "Замена SSD", "status": "Новая"},
    {"id": 4, "title": "Монитор", "status": "Готово"},
]


def build_ticket_card(ticket: dict, on_details):
    # TODO: оформите карточку и вызовите on_details(ticket["id"]).
    return ft.Card(content=ft.Container(padding=12, content=ft.Text(ticket["title"])))


def main(page: ft.Page):
    chosen = ft.Text("Выберите заявку")

    def show_details(ticket_id: int):
        chosen.value = f"Заявка №{ticket_id}"

    page.add(chosen, ft.Column(controls=[
        build_ticket_card(ticket, show_details) for ticket in TICKETS
    ]))


if __name__ == "__main__":
    ft.run(main)
