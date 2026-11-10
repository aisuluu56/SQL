# Практика 16 — Тема, цвета и единый визуальный стиль
# ЗАДАЧА: Панель настроек внешнего вида
# Откройте соответствующий lessons/16_theme.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Внешний вид"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    dark = ft.Switch(label="Тёмная тема")
    preview = ft.Card(content=ft.Container(padding=16, content=ft.Text("Предпросмотр")))

    def apply_settings(e=None):
        # TODO: переключите page.theme_mode.
        pass

    dark.on_change = apply_settings
    page.add(dark, preview)
    # TODO: Dropdown цветов и второе превью.


if __name__ == "__main__":
    ft.run(main)
