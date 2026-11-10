# Практика 24 — Модели данных и разделение ответственности
# ЗАДАЧА: Модель оборудования компьютерного класса
# Откройте соответствующий lessons/24_models.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

from dataclasses import dataclass
import flet as ft


@dataclass
class Computer:
    id: int
    room: str
    is_working: bool


def count_broken(computers: list[Computer]) -> int:
    # TODO: чистая функция без Flet.
    return 0


def main(page: ft.Page):
    computers = [Computer(1, "201", True), Computer(2, "203", False)]
    info = ft.Text()

    def render():
        info.value = f"Неисправных: {count_broken(computers)}"

    render()
    page.add(info)
    # TODO: список компьютеров и кнопку изменения состояния.


if __name__ == "__main__":
    ft.run(main)
