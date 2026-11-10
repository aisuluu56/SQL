"""Интерактивный курс Flet 1.0.5. Запуск: python course_app.py."""
import json
import subprocess
import sys
from pathlib import Path

import flet as ft

from progress_store import (
    load_progress,
    reset_all,
    reset_lesson,
    save_progress,
)

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))


def main(page: ft.Page):
    page.title = "Flet Academy — интерактивный учебник"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.INDIGO)
    page.padding = 16
    state = load_progress(valid_slugs=(item["slug"] for item in DATA))
    index = 0

    left_list = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO, spacing=4)
    counter = ft.Text(weight=ft.FontWeight.BOLD)
    progress_bar = ft.ProgressBar(value=0)
    lesson_title = ft.Text(size=25, weight=ft.FontWeight.BOLD)
    lesson_goal = ft.Text(color=ft.Colors.GREY_700)
    markdown = ft.Markdown(value="")
    quiz_title = ft.Text(size=16, weight=ft.FontWeight.BOLD)
    quiz_choices = ft.Column(spacing=6)
    feedback = ft.Text()
    done_button = ft.Button("Отметить практику выполненной")
    reset_lesson_button = ft.Button("Сбросить тему")
    reset_all_button = ft.TextButton("Сбросить весь прогресс")
    task_label = ft.Text(size=12)

    def notify(message: str) -> None:
        page.show_dialog(ft.SnackBar(ft.Text(message)))

    def render_menu() -> None:
        counter.value = f"Выполнено тем: {len(state['done'])}/{len(DATA)}"
        progress_bar.value = len(state["done"]) / len(DATA)
        reset_all_button.disabled = not (state["done"] or state["quiz"])
        left_list.controls = [
            ft.Button(
                f"{'✓' if item['slug'] in state['done'] else '•'} {i+1:02d}. {item['title']}",
                on_click=lambda e, selected=i: select(selected),
            ) for i, item in enumerate(DATA)
        ]

    def check(answer: int) -> None:
        item = DATA[index]
        if answer == item["quiz"][2]:
            state["quiz"].add(item["slug"])
            save_progress(state)
            feedback.value = "Верно! Выполните практику, затем зачтите тему."
            done_button.disabled = item["slug"] in state["done"]
            reset_lesson_button.disabled = False
            reset_all_button.disabled = False
        else:
            feedback.value = "Неверно — перечитайте объяснение и попробуйте ещё раз."

    def mark_done(e) -> None:
        item = DATA[index]
        if item["slug"] not in state["quiz"]:
            notify("Сначала ответьте на контрольный вопрос")
            return
        state["done"].add(item["slug"])
        save_progress(state)
        select(index)
        notify("Тема зачтена по самооценке: код автоматически не проверялся")

    def launch_task(e) -> None:
        path = ROOT / "tasks" / f"{DATA[index]['slug']}.py"
        try:
            subprocess.Popen([sys.executable, str(path)], cwd=str(ROOT))
            notify(f"Запущено отдельное окно: {path.name}")
        except OSError as exc:
            notify(f"Ошибка запуска: {exc}. Используйте терминал.")

    def select(i: int) -> None:
        nonlocal index
        index = i
        item = DATA[i]
        slug = item["slug"]
        render_menu()
        lesson_title.value = f"{i+1:02d}. {item['title']}"
        lesson_goal.value = item["goal"]
        markdown.value = (ROOT / "lessons" / f"{slug}.md").read_text(encoding="utf-8")
        task_label.value = f"Задание: tasks/{slug}.py"
        quiz_title.value = "Проверьте себя: " + item["quiz"][0]
        quiz_choices.controls = [
            ft.Button(f"{j+1}. {choice}", on_click=lambda e, answer=j: check(answer))
            for j, choice in enumerate(item["quiz"][1])
        ]
        feedback.value = (
            "Контрольный вопрос уже пройден. Можно выполнять практику."
            if slug in state["quiz"]
            else "Выберите вариант после изучения материала."
        )
        done_button.disabled = slug not in state["quiz"] or slug in state["done"]
        done_button.content = (
            "Тема зачтена (самопроверка)"
            if slug in state["done"] else "Отметить практику выполненной"
        )
        reset_lesson_button.disabled = slug not in state["done"] and slug not in state["quiz"]

    def reset_selected(slug: str) -> None:
        reset_lesson(state, slug)
        save_progress(state)
        page.pop_dialog()
        select(index)
        notify("Отметки темы сброшены. Теория, код задания и данные БД сохранены.")

    def confirm_reset_selected(e) -> None:
        item = DATA[index]
        slug = item["slug"]
        page.show_dialog(ft.AlertDialog(
            modal=True,
            title=ft.Text("Начать тему заново?"),
            content=ft.Text(
                f"Тема «{item['title']}»: будут сброшены ответ на тест и отметка "
                "о выполнении. Файл .py и база данных НЕ удалятся."
            ),
            actions=[
                ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
                ft.TextButton("Сбросить тему", on_click=lambda e: reset_selected(slug)),
            ],
        ))

    def reset_entire_course(e) -> None:
        reset_all(state)
        save_progress(state)
        page.pop_dialog()
        select(index)
        notify("Все отметки сброшены. Решения и данные PostgreSQL сохранены.")

    def confirm_reset_all(e) -> None:
        page.show_dialog(ft.AlertDialog(
            modal=True,
            title=ft.Text("Сбросить весь прогресс?"),
            content=ft.Text(
                "Будут сброшены результаты тестов и отметки выполнения для всех "
                "28 тем. Изменения кода в tasks/ и данные PostgreSQL сохранятся."
            ),
            actions=[
                ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
                ft.TextButton("Сбросить всё", on_click=reset_entire_course),
            ],
        ))

    done_button.on_click = mark_done
    reset_lesson_button.on_click = confirm_reset_selected
    reset_all_button.on_click = confirm_reset_all

    sidebar = ft.Container(width=310, padding=12, content=ft.Column(expand=True, controls=[
        ft.Text("Темы", size=21, weight=ft.FontWeight.BOLD),
        counter, progress_bar, reset_all_button, ft.Divider(), left_list,
    ]))
    body = ft.Column(expand=True, spacing=12, controls=[
        lesson_title, lesson_goal,
        ft.Row(wrap=True, controls=[
            ft.Button("Запустить .py", icon=ft.Icons.PLAY_ARROW, on_click=launch_task),
            done_button,
            reset_lesson_button,
        ]),
        task_label, ft.Divider(),
        ft.ListView(expand=True, controls=[markdown]),
        ft.Divider(), quiz_title, quiz_choices, feedback,
    ])
    page.add(ft.Row(expand=True, controls=[sidebar, ft.VerticalDivider(width=1), body]))
    select(0)


if __name__ == "__main__":
    ft.run(main)
