# Практика 12 — ListView и GridView: прокрутка и коллекции
# ЗАДАЧА: Галерея учебных дисциплин
# Откройте соответствующий lessons/12_scroll.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    subjects = ["Python", "SQL", "Flet", "Linux", "Git", "Web", "Go", "API", "Docker", "UI", "Тесты", "БД"]
    grid = ft.GridView(expand=True, runs_count=3, spacing=10, run_spacing=10)
    for index, subject in enumerate(subjects, start=1):
        grid.controls.append(ft.Container(
            content=ft.Text(f"{index}.{subject}"), padding=12, bgcolor=ft.Colors.BLUE_50, border_radius=8
        ))
    page.add(ft.Column(expand=True, controls=[ft.Text("Дисциплины", size=24), grid]))
    # TODO: сделайте три столбца и оформите карточки с номером.


if __name__ == "__main__":
    ft.run(main)
