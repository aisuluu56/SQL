# Практика 02 — Текст, иконки и оформление
# ЗАДАЧА: Карточка успеваемости
# Откройте соответствующий lessons/02_text_icons.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Успеваемость"
    page.padding = 25
    page.add(ft.Text("Моя дисциплина", size=26))
    page.add(ft.Icon(ft.Icons.AC_UNIT_SHARP, size=42, color=ft.Colors.AMBER_600))
    page.add(ft.Text("Жакыпбеков Айсулуу, предмет - математика, оценка - 5", size=26))
    # TODO: создайте информационную иерархию: иконка, оценка, подпись.


if __name__ == "__main__":
    ft.run(main)
