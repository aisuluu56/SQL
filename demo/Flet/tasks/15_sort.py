# Практика 15 — Сортировка, выбор и работа с коллекциями
# ЗАДАЧА: Рейтинг видеоигр
# Откройте соответствующий lessons/15_sort.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

GAMES = [
    {"id": 101, "name": "Portal", "rating": 9.6},
    {"id": 102, "name": "Celeste", "rating": 9.1},
    {"id": 103, "name": "Hades", "rating": 9.4},
]


def main(page: ft.Page):
    order = ft.Dropdown(label="Сортировать", options=[
        ft.DropdownOption(key="name", text="По названию"),
        ft.DropdownOption(key="rating", text="По оценке"),
    ], value="name")
    reverse = ft.Switch(label="Обратный порядок")
    result = ft.Text("Ничего не выбрано")
    cards = ft.Column()

    def render(e=None):
        cards.controls = [ft.Text(g["name"]) for g in GAMES]
        # TODO: sorted() и кнопка выбора по id.

    order.on_select = render
    reverse.on_change = render
    render()
    page.add(order, reverse, cards, result)
    # TODO: доведите список до 6 игр.


if __name__ == "__main__":
    ft.run(main)
