# Практика 03 — Row и Column: сборка макетов
# ЗАДАЧА: Шапка сайта библиотеки
# Откройте соответствующий lessons/03_layout.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Библиотека"
    page.padding = 24
    header = ft.Row(
        controls=[
            ft.Icon(ft.Icons.BOOK, size=30), 
            ft.Text("Электронная библиотека", weight=ft.FontWeight.BOLD, size=26), 
            ft.Text ("Каталог | Мои книги")
        ], 
        spacing=20
    )
    title = ft.Text("Добро пожаловать", weight=ft.FontWeight.BOLD, size=26)
    description = ft.Text("в ад.", size=10)
    page.add(ft.Column(
        controls=[
            header, 
            ft.Text("Приветсвие")
        ], 
        spacing=20
        )
    )
    # TODO: соберите настоящую шапку из Row и вложенных Column.


    page.add(
        title,
        description
    )
ft.run(main)
