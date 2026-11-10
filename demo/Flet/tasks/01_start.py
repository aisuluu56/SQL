# Практика 01 — Первое приложение и Page
# ЗАДАЧА: Экран-пропуск для экскурсии
# Откройте соответствующий lessons/01_start.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Aisuluu"
    page.padding = 16
    page.add(ft.Text("Экскурсия", size=24))
    page.add(ft.Text("Экскурсия", size=24))
    page.add(ft.Text("Экскурсия", size=24))
    # TODO: замените заголовок и добавьте ещё две строки.


if __name__ == "__main__":
    ft.run(main)
