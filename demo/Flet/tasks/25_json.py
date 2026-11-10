# Практика 25 — Локальное сохранение состояния в JSON
# ЗАДАЧА: Список покупок с сохранением
# Откройте соответствующий lessons/25_json.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import json
import os
from pathlib import Path
import flet as ft

DATA_DIR = Path(os.getenv("FLET_APP_STORAGE_DATA") or (Path.home() / ".flet_academy"))
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "shopping_list.json"


def load_items() -> list[str]:
    # TODO: загрузка с обработкой FileNotFoundError и JSONDecodeError.
    return []


def save_items(items: list[str]) -> None:
    # TODO: json.dumps + запись UTF-8.
    pass


def main(page: ft.Page):
    items = load_items()
    new_item = ft.TextField(label="Товар")
    current = ft.Column()

    def render():
        current.controls = [ft.Text(item) for item in items]

    def add_item(e):
        # TODO: добавление, save_items(), render().
        pass

    render()
    page.add(new_item, ft.Button("Добавить", on_click=add_item), current)


if __name__ == "__main__":
    ft.run(main)
