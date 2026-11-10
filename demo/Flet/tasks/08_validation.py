# Практика 08 — Валидация форм и ошибки ввода
# ЗАДАЧА: Проверка регистрации на олимпиаду
# Откройте соответствующий lessons/08_validation.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Регистрация на олимпиаду"
    fio = ft.TextField(label="ФИО")
    course = ft.TextField(label="Курс (1–4)")
    feedback = ft.Text()

    def register(e):
        fio.error = None
        course.error = None

        try:
            fio_len  = len(fio.value or "")
            if fio_len < 3 and not (1 <= int(course.value) <= 4):
                raise ValueError

            feedback.value = f"Символов в ФИО: {fio_len} || Курс студента: {course.value}"

        except ValueError:
            fio.error = "Введите больше 3 символов"
            course.error = "Введите курс от 1 до 4"
            feedback.value = "Форма еще не проверено"
        
        # TODO: проверьте длину ФИО, число и допустимый диапазон.
        #feedback.value = "Форма ещё не проверена"

    page.add(fio, course, ft.Button("Зарегистрироваться", on_click=register), feedback)


if __name__ == "__main__":
    ft.run(main)
