# Практика 04 — Container, рамки, отступы и карточки
# ЗАДАЧА: Бейдж участника конференции
# Откройте соответствующий lessons/04_container.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft


def main(page: ft.Page):
    page.title = "Бейдж"
    page.padding = 24
    page.add(ft.Container(
        padding=20, margin=10, border_radius=16,
        bgcolor=ft.Colors.BLUE_50,
        content=ft.Column(
            controls=
                [
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.PERSON, size=30),
                            ft.Column(
                                controls=
                                [
                                    ft.Text("Активист", weight=ft.FontWeight.BOLD, size=26), 
                                    ft.Text ("Жакыпбекова Айсулуу"),
                                    ft.Text("Финансовый колледж 35")

                                ],
                                spacing=10
                            ),
                        ]
                    )
                ],
            
            ),
            width=300
        )
    )
        #content=ft.Text("Участник"),
        #padding=12,
        #bgcolor=ft.Colors.BLUE_50,
    # TODO: оформите полноценный бейдж вместо одной надписи.


if __name__ == "__main__":
    ft.run(main)

