# Практика 21 — View и маршруты: многоэкранное приложение
# ЗАДАЧА: Маршруты для списка музеев
# Откройте соответствующий lessons/21_routes.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

MUSEUMS = {"1": "Музей космоса", "2": "Музей истории"}


def main(page: ft.Page):
    async def go_to_museum(museum_id: str):
        # TODO: await page.push_route(f"/museum/{museum_id}")
        pass

    def route_changed(e=None):
        page.views.clear()
        page.views.append(ft.View(route="/", controls=[
            ft.Text("Музеи", size=26),
            # TODO: создайте по кнопке для каждого музея.
        ]))
        # TODO: дополняйте стек View при маршрутах /museum/1 и /museum/2.

    page.on_route_change = route_changed
    route_changed()


if __name__ == "__main__":
    ft.run(main)
