import flet as ft


def main(page: ft.Page):
  page.title = "Обводка текста во Flet"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.bgcolor = ft.colors.BLUE_GREY_900

  # Функция для создания текста с обводкой
  def stroked_text(
      text, text_size=40, text_color="white", stroke_color="black", stroke_width=2
  ):
    # Создаем базовые стили для текста обводки и основного текста
    stroke_style = ft.TextStyle(
        size=text_size, color=stroke_color, weight=ft.FontWeight.BOLD
    )
    main_style = ft.TextStyle(
        size=text_size, color=text_color, weight=ft.FontWeight.BOLD
    )

    return ft.Stack(
        controls=[
            # Сдвиги по диагоналям для создания плотной обводки
            ft.Text(
                text,
                style=stroke_style,
                offset=ft.Offset(-stroke_width / 100, -stroke_width / 100),
            ),
            ft.Text(
                text,
                style=stroke_style,
                offset=ft.Offset(stroke_width / 100, -stroke_width / 100),
            ),
            ft.Text(
                text,
                style=stroke_style,
                offset=ft.Offset(-stroke_width / 100, stroke_width / 100),
            ),
            ft.Text(
                text,
                style=stroke_style,
                offset=ft.Offset(stroke_width / 100, stroke_width / 100),
            ),
            # Основной текст по центру сверху
            ft.Text(text, style=main_style),
        ]
    )

  # Добавляем кастомный текст на страницу
  page.add(
      stroked_text(
          text="Привет, Flet!",
          text_size=50,
          text_color=ft.colors.YELLOW,
          stroke_color=ft.colors.BLACK,
          stroke_width=2,  # Чем больше число, тем сильнее сдвиг
      )
  )

if __name__ == "__main__":
    ft.run(main) 
