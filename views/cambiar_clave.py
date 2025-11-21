import flet as ft
from database.db_manager import DatabaseManager


class CambiarClaveView:
    def __init__(self, page, usuario_data, on_volver):
        self.page = page
        self.usuario_data = usuario_data
        self.on_volver = on_volver
        self.db = DatabaseManager()
        self.container = None
    
    def build(self):
        titulo = ft.Text(
            "Cambiar Contraseña",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
        
        self.txt_clave_actual = ft.TextField(
            label="Contraseña actual",
            password=True,
            can_reveal_password=True,
            width=400,
            height=65,
            text_size=16,
            border_radius=12,
            border_color=ft.Colors.ORANGE_200,
            focused_border_color=ft.Colors.ORANGE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.ORANGE_400,
            prefix_icon=ft.Icons.LOCK,
            autofocus=True
        )
        
        self.txt_clave_nueva = ft.TextField(
            label="Nueva contraseña",
            password=True,
            can_reveal_password=True,
            width=400,
            height=65,
            text_size=16,
            border_radius=12,
            border_color=ft.Colors.ORANGE_200,
            focused_border_color=ft.Colors.ORANGE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.ORANGE_400,
            prefix_icon=ft.Icons.LOCK_OPEN
        )
        
        self.txt_confirmar_nueva = ft.TextField(
            label="Confirmar nueva contraseña",
            password=True,
            can_reveal_password=True,
            width=400,
            height=65,
            text_size=16,
            border_radius=12,
            border_color=ft.Colors.ORANGE_200,
            focused_border_color=ft.Colors.ORANGE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.ORANGE_400,
            prefix_icon=ft.Icons.LOCK_OUTLINE
        )
        
        self.txt_mensaje = ft.Container(
            content=ft.Text(
                value="",
                size=14,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_500
            ),
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.RED),
            padding=12,
            border_radius=10,
            visible=False,
            width=400
        )
        
        self.btn_cambiar = ft.ElevatedButton(
            text="Cambiar Contraseña",
            width=400,
            height=55,
            on_click=self.cambiar_clave,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.ORANGE_700,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4
            )
        )
        
        btn_volver = ft.OutlinedButton(
            text="Volver al Dashboard",
            icon=ft.Icons.ARROW_BACK,
            width=400,
            on_click=self.volver_dashboard,
            style=ft.ButtonStyle(
                color=ft.Colors.BLUE_400,
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(2, ft.Colors.BLUE_400)
            )
        )
        
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=30),
                    ft.Text("NovaBank", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Container(height=40),
                    titulo,
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                self.txt_clave_actual,
                                ft.Container(height=15),
                                self.txt_clave_nueva,
                                ft.Container(height=15),
                                self.txt_confirmar_nueva,
                                ft.Container(height=20),
                                self.btn_cambiar,
                                ft.Container(height=15),
                                self.txt_mensaje,
                                ft.Container(height=15),
                                btn_volver
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0
                        ),
                        padding=40,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
                        width=500
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                scroll=ft.ScrollMode.AUTO
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#0a1929", "#1a2332", "#0d3d56", "#114357"]
            ),
            padding=20,
            expand=True
        )
        
        return self.container
    
    def cambiar_clave(self, e):
        self.txt_mensaje.visible = False
        self.page.update()
        
        clave_actual = self.txt_clave_actual.value
        clave_nueva = self.txt_clave_nueva.value
        confirmar_nueva = self.txt_confirmar_nueva.value
        
        if not clave_actual or not clave_nueva or not confirmar_nueva:
            self.mostrar_mensaje("Por favor completa todos los campos", ft.Colors.RED)
            return
        
        if clave_nueva != confirmar_nueva:
            self.mostrar_mensaje("Las contraseñas nuevas no coinciden", ft.Colors.RED)
            return
        
        if len(clave_nueva) < 4:
            self.mostrar_mensaje("La nueva contraseña debe tener al menos 4 caracteres", ft.Colors.RED)
            return
        
        resultado = self.db.cambiar_clave(
            usuario_id=self.usuario_data['id'],
            clave_actual=clave_actual,
            clave_nueva=clave_nueva
        )
        
        if resultado["exito"]:
            self.mostrar_mensaje(resultado["mensaje"], ft.Colors.GREEN)
            self.txt_clave_actual.value = ""
            self.txt_clave_nueva.value = ""
            self.txt_confirmar_nueva.value = ""
            self.page.update()
        else:
            self.mostrar_mensaje(resultado["mensaje"], ft.Colors.RED)
    
    def mostrar_mensaje(self, mensaje, color):
        self.txt_mensaje.content.value = mensaje
        self.txt_mensaje.content.color = ft.Colors.WHITE
        self.txt_mensaje.bgcolor = ft.Colors.with_opacity(0.9, color)
        self.txt_mensaje.visible = True
        self.page.update()
    
    def volver_dashboard(self, e):
        self.on_volver(self.usuario_data)
