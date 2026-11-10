# Практика 20 — Tabs, TabBar и TabBarView
# ЗАДАЧА: Вкладки карточки учебного курса
# Откройте соответствующий lessons/20_tabs.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Курс"
    tabs = ft.Tabs(length=2, expand=True, content=ft.Column(expand=True, controls=[
        ft.TabBar(tabs=[ft.Tab(label="Программа"), ft.Tab(label="Преподаватель")]),
        ft.TabBarView(expand=True, controls=[
            ft.Text("Темы курса"),
            ft.Text("Имя преподавателя"),
        ]),
    ]))
    page.add(tabs)
    # TODO: третья вкладка и полноценное содержимое всех вкладок.


if __name__ == "__main__":
    ft.run(main)
