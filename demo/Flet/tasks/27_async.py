# Практика 27 — Асинхронные операции и индикаторы загрузки
# ЗАДАЧА: Имитация обработки заявок
# Откройте соответствующий lessons/27_async.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import asyncio
import flet as ft


def main(page: ft.Page):
    status = ft.Text("Ожидание")
    progress = ft.ProgressBar(value=0, visible=False)

    async def process(e):
        # TODO: async цикл из пяти шагов, await asyncio.sleep(0.4).
        # TODO: обновляйте прогресс и отправляйте промежуточные изменения через page.update().
        # TODO: отключайте кнопку; finally восстанавливайте её.
        status.value = "Операция пока не реализована"

    start = ft.Button("Обработать пакет", on_click=process)
    page.add(start, progress, status)


if __name__ == "__main__":
    ft.run(main)
