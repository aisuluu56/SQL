# Практика 05 — Кнопки и обработчики событий
# ЗАДАЧА: Пульт светового сигнала
# Откройте соответствующий lessons/05_events.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Пульт"
    status = ft.Text("Сигнал выключен", size=24)

    def turn_on(e):
        status.value = "Сигнал включен" 
        status.color = ft.Colors.GREEN
        page.update()

    def turn_off(e):
            status.value = "Сигнал выключен" 
            status.color = ft.Colors.RED
            page.update()

    def show_403(e):
            status.value = "403 Доступ запрепщен" 
            status.color = ft.Colors.ORANGE
            page.update()
        # TODO: изменить текст и цвет индикатора.
    pass

    page.add(
          status,
          ft.Row(controls=[
             ft.Button("Включить", on_click=turn_on),
             ft.Button("Выключить", on_click=turn_off),
             ft.Button("403", on_click=show_403)
            ]
          )
    )
    # TODO: добавить ещё 2 кнопки с обработчиками.


if __name__ == "__main__":
    ft.run(main)
