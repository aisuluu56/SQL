# Практика 19 — NavigationBar: переключение экранов
# ЗАДАЧА: Мини-приложение городской среды
# Откройте соответствующий lessons/19_navigation.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Мой город"
    content = ft.Column(controls=[ft.Text("События", size=24)])

    def show_screen(e):
        # TODO: отображайте разные элементы в зависимости от selected_index.
        pass

    page.navigation_bar = ft.NavigationBar(destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="События"),
        ft.NavigationBarDestination(icon=ft.Icons.PLACE, label="Места"),
        ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Профиль"),
    ], on_change=show_screen)
    page.add(content)


if __name__ == "__main__":
    ft.run(main)
