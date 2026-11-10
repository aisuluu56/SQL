# Практика 09 — Checkbox и Switch: логические значения
# ЗАДАЧА: Выбор услуг в мастерской
# Откройте соответствующий lessons/09_boolean.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Услуги"
    diagnostics = ft.Checkbox(label="Диагностика", value=False)
    clean = ft.Checkbox(label="Очистка", value=False)
    install = ft.Checkbox(label="Установка ПО", value=False)
    rush_order = ft.Switch(label = "Срочный заказ", value=False)

    counter = ft.Text("Выбрано: 0")

    def recalc(e):
        selected_count = sum([
            diagnostics.value,
            clean.value,
            install.value
        ])
        counter.value = f"Выбрано: {selected_count}"
        page.update()

    for checkbox in [diagnostics, clean, install]:
        checkbox.on_change = recalc
    
    for switch in [rush_order]:
        switch.on_change = recalc

    diagnostics.on_change = recalc
    page.add(diagnostics, clean, install, rush_order, counter)


if __name__ == "__main__":
    ft.run(main)
