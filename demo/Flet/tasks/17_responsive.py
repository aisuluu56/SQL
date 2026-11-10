# Практика 17 — Адаптивная компоновка ResponsiveRow
# ЗАДАЧА: Дашборд учебной платформы
# Откройте соответствующий lessons/17_responsive.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

METRICS = [("Студенты", 128), ("Группы", 8), ("Курсы", 14), ("Тесты", 32)]


def main(page: ft.Page):
    page.title = "Показатели"
    cards = []
    for name, count in METRICS:
        cards.append(ft.Container(
            col={ft.ResponsiveRowBreakpoint.XS: 12},
            padding=18,
            content=ft.Text(f"{name}: {count}"),
        ))
    page.add(ft.ResponsiveRow(controls=cards, spacing=12, run_spacing=12))
    # TODO: breakpoint MD и LG, оформление и иконки.


if __name__ == "__main__":
    ft.run(main)
