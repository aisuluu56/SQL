# Практика 07 — TextField: ввод и изменение текста
# ЗАДАЧА: Генератор электронного бейджа
# Откройте соответствующий lessons/07_textfields.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор бейджа"
    name_input = ft.TextField(label="Имя")
    job_input = ft.TextField(label="Должность")
    result = ft.Text("Бейдж ещё не создан")

    def build_badge(e):
        if name_input.value.strip() == "" or job_input.value.strip() == "Бейжд создан":
            result.value = "Заполните оба поля"
            result.color = ft.Colors.RED
        else:
            result.value = f"Бейжд создан: {name_input.value} - {job_input.value}"
            result.color = ft.Colors.GREEN
            page.update

        # TODO: проверьте имя, получите должность и измените result.value.
        pass

    page.add(name_input,
             job_input,
             ft.Button("Создать бейдж", on_click=build_badge),
             result
        )
    # TODO: добавьте поле «Должность».


if __name__ == "__main__":
    ft.run(main)
