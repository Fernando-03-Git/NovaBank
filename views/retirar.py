import flet as ft
from logic.transacciones import TransaccionesManager


class RetirarView:
    def __init__(self, page, usuario_data, on_volver):
        self.page = page
        self.usuario_data = usuario_data
        self.on_volver = on_volver
        self.transacciones = TransaccionesManager()
        self.container = None
    
    def build(self):
        titulo = ft.Text(
            "Retirar",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
        
        self.txt_saldo_actual = ft.Text(
            f"Saldo disponible: ${self.usuario_data['saldo']:,.2f}",
            size=18,
            color=ft.Colors.BLUE_400,
            weight=ft.FontWeight.W_500
        )
        
        self.txt_monto = ft.TextField(
            label="Monto a retirar",
            hint_text="Ingresa el monto",
            width=400,
            height=65,
            text_size=16,
            border_radius=12,
            border_color=ft.Colors.BLUE_200,
            focused_border_color=ft.Colors.BLUE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.BLUE_400,
            prefix_text="$ ",
            prefix_icon=ft.Icons.MONEY_OFF,
            keyboard_type=ft.KeyboardType.NUMBER,
            autofocus=True
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
        
        self.btn_retirar = ft.ElevatedButton(
            text="Retirar",
            width=400,
            height=55,
            on_click=self.realizar_retiro,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_700,
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
                    ft.Container(height=10),
                    self.txt_saldo_actual,
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                self.txt_monto,
                                ft.Container(height=20),
                                self.btn_retirar,
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
    
    def realizar_retiro(self, e):
        self.txt_mensaje.visible = False
        self.page.update()
        
        if not self.txt_monto.value:
            self.mostrar_mensaje("Por favor ingresa un monto", ft.Colors.RED)
            return
        
        try:
            monto = float(self.txt_monto.value)
        except ValueError:
            self.mostrar_mensaje("El monto debe ser un número válido", ft.Colors.RED)
            return
        
        if monto <= 0:
            self.mostrar_mensaje("El monto debe ser mayor a 0", ft.Colors.RED)
            return
        
        resultado = self.transacciones.retirar(
            usuario_id=self.usuario_data['id'],
            monto=monto
        )
        
        if resultado["exito"]:
            self.usuario_data["saldo"] = resultado["nuevo_saldo"]
            self.txt_saldo_actual.value = f"Saldo disponible: ${resultado['nuevo_saldo']:,.2f}"
            self.mostrar_mensaje(resultado["mensaje"], ft.Colors.GREEN)
            self.txt_monto.value = ""
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
