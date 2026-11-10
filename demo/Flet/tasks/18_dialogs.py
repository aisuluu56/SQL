# Практика 18 — SnackBar и AlertDialog: обратная связь
# ЗАДАЧА: Подтверждение удаления профиля
# Откройте соответствующий lessons/18_dialogs.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Профиль"
    status = ft.Text("Профиль существует")

    def request_delete(e):
        # TODO: открыть AlertDialog с кнопками «Удалить» и «Отмена».
        page.show_dialog(ft.SnackBar(ft.Text("Нужно добавить подтверждение")))

    page.add(status, ft.Button("Удалить профиль", on_click=request_delete))


if __name__ == "__main__":
    ft.run(main)
