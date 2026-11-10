# Практика 10 — Dropdown и Slider: выбор одного значения
# ЗАДАЧА: Конфигуратор сложности теста
# Откройте соответствующий lessons/10_choice.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Генератор теста"
    mode = ft.Dropdown(label="Режим", options=[
        ft.DropdownOption(key="practice", text="Тренировка"),
        ft.DropdownOption(key="control", text="Контроль"),
        ft.DropdownOption(key="exam", text="Экзамен")
    ])
    result = ft.Text("Тест не настроен")
    question = ft.Slider(min=5, max=30, value=15, divisions=5)

    def show(e):
        if mode.value == None:
            result
        else:
            result.value = f"Режим: {mode.value} || Вопросов: {question.value}"


    page.add(mode, question, ft.Button("Создать тест", on_click=show), result)
    # TODO: добавьте ещё 2 режима, Slider и обработчик кнопки.


if __name__ == "__main__":
    ft.run(main)