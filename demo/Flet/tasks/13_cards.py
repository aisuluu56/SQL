# Практика 13 — Card, ListTile и изображения
# ЗАДАЧА: Каталог компьютерных комплектующих
# Откройте соответствующий lessons/13_cards.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

PRODUCTS = [
    {"name": "SSD 512 ГБ", "price": 4200, "stock": 7},
    {"name": "ОЗУ 16 ГБ", "price": 3100, "stock": 0},
    {"name": "Мышь", "price": 890, "stock": 18},
    {"name": "Клавиатура", "price": 2200, "stock": 3},
]


def main(page: ft.Page):
    page.title = "Комплектующие"
    cards = ft.Column(spacing=10)
    for product in PRODUCTS:
        cards.controls.append(ft.Card(content=ft.Container(
            padding=12, content=ft.Text(product["name"]),
        )))
    page.add(cards)
    # TODO: иконка, цена, остаток и условное выделение.


if __name__ == "__main__":
    ft.run(main)
