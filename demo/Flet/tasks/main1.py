import flet as ft

def main(page: ft.Page):
    page.title = "Карточка товара"
    page.padding = 50
    
    page.add(ft.Container(
        padding=24,
        margin=10,
        border_radius=30,
        bgcolor=ft.Colors.WHITE_10,
        content=ft.Row(spacing=80,
        controls= [ft.Icon(ft.Icons.IMAGE, size=80),
        ft.Column(controls=[
                ft.Text("Кроссовки детские", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Кроссовки детские"),
                ft.Text("Кроссовки детские «Звёздочка» экокожа. Производитель: ООО «Малыш-Спорт», г. Смоленск"),
                ft.Container(
                        content=ft.Column(
                                controls=[
                                        ft.Text("Состав"),
                                        ft.Text("Верх —a экокожа (полиуретан на хлопковой основе), подкладка — хлопок 100%, подошва — ПВХ")
                                
                                ],
                                spacing=5
                        ),
                        padding=10
                        bgcolor=ft.Colors.WHITE_10,
                )
        ]),
        ft.Column
        ])))
                                        


'''





        ft.Container(
            padding=24,
            margin=10,
            border_radius=30,
            bgcolor=ft.Colors.WHITE_10,
            content=ft.Row( spacing=80, controls=[ ft.Icon(ft.Icons.IMAGE, size=30)
                            
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Text("Детская обувь", weight=ft.FontWeight.BOLD, size=10, color = ft.Colors.BLUE_400),
                                                bgcolor=ft.Colors.BLUE_50,
                                                padding=20 
                                                )
                                            ft.Text("Кроссовки", weight=ft.FontWeight.BOLD, size=10, color = ft.Colors.BLUE_400),
                                        ],
                                        spacing=10
                                    ),
                                    ft.Text("Жакыпбекова Айсулуу"),
                                    ft.Text("Финансовый колледж 35")
                                ],
                                spacing=10
                            ),
                        ]
                    )
                ],
            ),
            width=600
        )
    )

if __name__ == "__main__":
    ft.run(main) 
'''