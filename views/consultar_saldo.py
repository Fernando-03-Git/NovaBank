import flet as ft
from logic.transacciones import TransaccionesManager


class ConsultarSaldoView:
    def __init__(self, page, usuario_data, on_volver):
        self.page = page
        self.usuario_data = usuario_data
        self.on_volver = on_volver
        self.transacciones = TransaccionesManager()
        self.container = None
    
    def build(self):
        titulo = ft.Text(
            "Consultar Saldo",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
        
        # Info del usuario
        info_usuario = ft.Column(
            controls=[
                ft.Text(
                    f"@{self.usuario_data['usuario']}",
                    size=18,
                    color=ft.Colors.GREY_400,
                    weight=ft.FontWeight.W_500
                ),
                ft.Text(
                    f"{self.usuario_data['nombre']} {self.usuario_data['apellido']}",
                    size=16,
                    color=ft.Colors.GREY_300
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        )
        
        # Tarjeta de saldo grande
        self.tarjeta_saldo = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(
                        ft.Icons.ACCOUNT_BALANCE_WALLET,
                        size=50,
                        color=ft.Colors.CYAN_400
                    ),
                    ft.Container(height=15),
                    ft.Text(
                        "Saldo Actual",
                        size=16,
                        color=ft.Colors.GREY_300
                    ),
                    ft.Text(
                        f"${self.usuario_data['saldo']:,.2f}",
                        size=52,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_400
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=40,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
            border=ft.border.all(2, ft.Colors.with_opacity(0.3, ft.Colors.CYAN_400)),
            width=450
        )
        
        # Botón refrescar
        btn_refrescar = ft.ElevatedButton(
            text="Refrescar Saldo",
            icon=ft.Icons.REFRESH,
            width=300,
            height=50,
            on_click=self.refrescar_saldo,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.CYAN_700,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4
            )
        )
        
        btn_volver = ft.OutlinedButton(
            text="Volver al Dashboard",
            icon=ft.Icons.ARROW_BACK,
            width=300,
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
                    ft.Container(height=20),
                    info_usuario,
                    ft.Container(height=40),
                    self.tarjeta_saldo,
                    ft.Container(height=40),
                    btn_refrescar,
                    ft.Container(height=15),
                    btn_volver
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
    
    def refrescar_saldo(self, e):
        resultado = self.transacciones.consultar_saldo(self.usuario_data['id'])
        
        if resultado["exito"]:
            self.usuario_data["saldo"] = resultado["saldo"]
            self.tarjeta_saldo.content.controls[3].value = f"${resultado['saldo']:,.2f}"
            self.page.update()
    
    def volver_dashboard(self, e):
        self.on_volver(self.usuario_data)
