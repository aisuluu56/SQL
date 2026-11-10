# Практика 11 — Динамическое добавление и удаление элементов
# ЗАДАЧА: Список фильмов «Посмотреть»
# Откройте соответствующий lessons/11_dynamic.md перед работой.
# TODO помечает места, которые нужно дополнить самостоятельно.

import flet as ft

def main(page: ft.Page):
    movies = ["Интерстеллар", "Контакт", "Начало"]
    new_movie = ft.TextField(label="Новый фильм")
    movie_list = ft.Column()

    def redraw():
        movie_list.controls.clear()
        for i in range(len(movies)):
            movie_list.controls.append(
                ft.Row([
                    ft.Text(movies[i]),
                    ft.Button(f"Удалить{i+1}", on_click=lambda e, idx=1:
                              delete_movie(idx))
                ])
            )

    def delete_movie(index):
        del movies[index]
       
        redraw()

    def add_movie(e):
        if new_movie.value.strip():
            movies.append(new_movie.value.strip())
            redraw()

    page.add(new_movie, ft.Button("Добавить", on_click=add_movie), movie_list)

if __name__ == "__main__":
    ft.run(main)
