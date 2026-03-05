import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.bgcolor = "#101416"
    page.max_width = "900"
    page.scroll = "auto"
    
    titulo = ft.Text(
        value="Registro de participantes",
        size=40,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )

    div = ft.Divider(height=10, thickness=2, color=ft.Colors.WHITE)

    subtitle = ft.Text(
        value="Ingresa aqui tus datos",
        size=25,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    np = ft.TextField(
        label="Nombre del Participante",
        hint_text="Ingresa aqui tu Numbre",
        value="",
        max_length=50,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.WHITE_10,
        border_color=ft.Colors.WHITE
    )
    
    ce = ft.TextField(
        label="Correo Electronico",
        hint_text="Ingresa aqui tu Correo Electronico",
        value="",
        max_length=50,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.WHITE_10,
        border_color=ft.Colors.WHITE
    )

    select = ft.Dropdown(
        label="Taller de Interes",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK,
        border_color=ft.Colors.WHITE,
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )
    
    pago = ft.Text(
        value="Forma de Pago",
        size=20,
        color=ft.Colors.WHITE,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    pago2 = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Pago Completo", label="Pago Completo", label_style = ft.TextStyle(color = "white")),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas", label_style = ft.TextStyle(color = "white")),
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand=True),
        value="Pago Completo"
    )
    
    ver = ft.Checkbox(
        label="Requiere computadora Portatil",
        label_style = ft.TextStyle(color = "white"),
        value=False,
        tristate=False,
        check_color=ft.Colors.BLACK,
        fill_color=ft.Colors.WHITE,
    )

    
    exp = ft.Text(
        value="Nivel de experiencia",
        size=20,
        color=ft.Colors.WHITE,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    )
    
    slider = ft.Slider(
        min=1,
        max=5,
        divisions=4,
        value=1,
        label="{value}"
    )

    def usuarios():
        if np.value != "":
            resultados.value = (
                f"{np.value}\n"
                f"{ce.value}\n"
                f"{select.value}\n"
                f"{pago2.value}\n"
                f"{ver.value}\n"
                f"{slider.value}\n"
            )
        page.update()
            
    boton = ft.TextButton(
        content = ft.Text("Add User", color=ft.Colors.WHITE),
        on_click=usuarios
    )
        
    resultados = ft.Text(
            value = "",
            color=ft.Colors.WHITE
        )
    
    page.add(
        titulo,
        div,
        subtitle,
        np,
        ce,
        select,
        pago,
        pago2,
        ver,
        exp,
        slider,
        boton,
        resultados
    )


ft.run(main)