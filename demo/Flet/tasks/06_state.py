# Практика 06 — Состояние приложения и обновление UI
# ЗАДАЧА: Счётчик свободных мест
# Откройте соответствующий lessons/06_state.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    seats = 12
    max_seats = 12
    available = ft.Text(f"Свободно: {seats}", size=24)

    def render():
        available.value = f"Счетчик свободных мест: {seats}"
        # TODO: единое место обновления интерфейса.
    

    def reserve(e):
        nonlocal seats
        seats = max(0, seats -1)
        render()

    def leave(e):
        nonlocal seats
        seats= min(max_seats, seats + 1)
        render()
        # TODO: уменьшить seats без выхода за границы и вызвать render.
    

    page.add(available,
              ft.Row(controls =[
                  ft.Button("Занять 1", on_click = reserve),
                  ft.Button("Освободить 1", on_click = leave),
              ])
            )
    render()
    # TODO: реализуйте освобождение места.


if __name__ == "__main__":
    ft.run(main)
