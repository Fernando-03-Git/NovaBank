import flet as ft
from logic.transacciones import TransaccionesManager


class HistorialView:
    def __init__(self, page, usuario_data, on_volver):
        self.page = page
        self.usuario_data = usuario_data
        self.on_volver = on_volver
        self.transacciones = TransaccionesManager()
        self.container = None
    
    def build(self):
        titulo = ft.Text(
            "Historial de Transacciones",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
        
        # Obtener transacciones
        resultado = self.transacciones.obtener_historial(self.usuario_data['id'], limite=20)
        
        if resultado["exito"] and resultado["transacciones"]:
            lista_transacciones = self.crear_lista_transacciones(resultado["transacciones"])
        else:
            lista_transacciones = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.Icons.RECEIPT_LONG, size=60, color=ft.Colors.GREY_600),
                        ft.Container(height=15),
                        ft.Text(
                            "No hay transacciones registradas",
                            size=16,
                            color=ft.Colors.GREY_400
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=40
            )
        
        btn_refrescar = ft.ElevatedButton(
            text="Refrescar",
            icon=ft.Icons.REFRESH,
            width=250,
            height=50,
            on_click=self.refrescar_historial,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.INDIGO_700,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4
            )
        )
        
        btn_volver = ft.OutlinedButton(
            text="Volver al Dashboard",
            icon=ft.Icons.ARROW_BACK,
            width=250,
            on_click=self.volver_dashboard,
            style=ft.ButtonStyle(
                color=ft.Colors.BLUE_400,
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(2, ft.Colors.BLUE_400)
            )
        )
        
        self.lista_container = ft.Container(
            content=lista_transacciones,
            width=600,
            height=400,
            padding=20,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE)
        )
        
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=30),
                    ft.Text("NovaBank", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Container(height=40),
                    titulo,
                    ft.Container(height=30),
                    btn_refrescar,
                    ft.Container(height=20),
                    self.lista_container,
                    ft.Container(height=20),
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
    
    def crear_lista_transacciones(self, transacciones):
        """Crea la lista visual de transacciones"""
        items = []
        
        for t in transacciones:
            # Determinar color e icono según tipo
            if t['tipo'] == 'DEPOSITO':
                color = ft.Colors.GREEN_400
                icono = ft.Icons.ARROW_DOWNWARD
                bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.GREEN)
            elif t['tipo'] == 'RETIRO':
                color = ft.Colors.RED_400
                icono = ft.Icons.ARROW_UPWARD
                bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.RED)
            elif t['tipo'] == 'TRANSFERENCIA_ENVIADA':
                color = ft.Colors.ORANGE_400
                icono = ft.Icons.SEND
                bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.ORANGE)
            elif t['tipo'] == 'TRANSFERENCIA_RECIBIDA':
                color = ft.Colors.BLUE_400
                icono = ft.Icons.CALL_RECEIVED
                bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.BLUE)
            else:
                color = ft.Colors.GREY_400
                icono = ft.Icons.ACCOUNT_BALANCE_WALLET
                bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.GREY)
            
            item = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(icono, size=24, color=color),
                            width=50,
                            height=50,
                            border_radius=10,
                            bgcolor=bgcolor,
                            alignment=ft.alignment.center
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    t['descripcion'],
                                    size=14,
                                    weight=ft.FontWeight.W_500,
                                    color=ft.Colors.WHITE
                                ),
                                ft.Text(
                                    t['fecha'],
                                    size=12,
                                    color=ft.Colors.GREY_400
                                )
                            ],
                            spacing=3,
                            expand=True
                        ),
                        ft.Text(
                            f"${t['monto']:,.2f}",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=color
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=15
                ),
                padding=15,
                border_radius=12,
                bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                border=ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.WHITE))
            )
            items.append(item)
        
        return ft.Column(
            controls=items,
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )
    
    def refrescar_historial(self, e):
        """Refresca el historial de transacciones"""
        resultado = self.transacciones.obtener_historial(self.usuario_data['id'], limite=20)
        
        if resultado["exito"] and resultado["transacciones"]:
            nueva_lista = self.crear_lista_transacciones(resultado["transacciones"])
        else:
            nueva_lista = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.Icons.RECEIPT_LONG, size=60, color=ft.Colors.GREY_600),
                        ft.Container(height=15),
                        ft.Text(
                            "No hay transacciones registradas",
                            size=16,
                            color=ft.Colors.GREY_400
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=40
            )
        
        self.lista_container.content = nueva_lista
        self.page.update()
    
    def volver_dashboard(self, e):
        self.on_volver(self.usuario_data)
