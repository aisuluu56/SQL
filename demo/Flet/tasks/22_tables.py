# Практика 22 — DataTable: табличные данные и сортировка
# ЗАДАЧА: Табель посещаемости
# Откройте соответствующий lessons/22_tables.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

STUDENTS = [
    {"name": "Анна", "absences": 1, "grade": 4.8},
    {"name": "Борис", "absences": 5, "grade": 3.9},
    {"name": "Вера", "absences": 0, "grade": 4.6},
]


def main(page: ft.Page):
    def make_rows():
        return [ft.DataRow(cells=[
            ft.DataCell(ft.Text(s["name"])),
            ft.DataCell(ft.Text(str(s["absences"]))),
        ]) for s in STUDENTS]

    table = ft.DataTable(columns=[
        ft.DataColumn(label=ft.Text("Студент")),
        ft.DataColumn(label=ft.Text("Пропуски")),
    ], rows=make_rows())
    page.add(ft.Row(scroll=ft.ScrollMode.AUTO, controls=[table]))
    # TODO: третий столбец, больше студентов и обработчик on_sort.


if __name__ == "__main__":
    ft.run(main)
