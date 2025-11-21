import flet as ft


class DashboardView:
    def __init__(self, page, usuario_data, on_logout, on_ir_vista):
        self.page = page
        self.usuario_data = usuario_data
        self.on_logout = on_logout
        self.on_ir_vista = on_ir_vista
        self.container = None
    
    def build(self):
        # ========== HEADER CON INFO DEL USUARIO ==========
        header = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        f"{self.usuario_data['nombre']} {self.usuario_data['apellido']}",
                                        size=32,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE
                                    ),
                                    ft.Text(
                                        f"@{self.usuario_data['usuario']}",
                                        size=15,
                                        color=ft.Colors.GREY_400
                                    )
                                ],
                                spacing=5
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=20),
                    # Tarjeta de saldo
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Saldo disponible",
                                    size=14,
                                    color=ft.Colors.GREY_300,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    f"${self.usuario_data['saldo']:,.2f}",
                                    size=42,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREEN_400,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8
                        ),
                        padding=30,
                        border_radius=16,
                        bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                        border=ft.border.all(2, ft.Colors.with_opacity(0.2, ft.Colors.GREEN_400)),
                        width=400
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            padding=20
        )
        
        # ========== BOTONES DE ACCIONES ==========
        # Fila 1: Depositar y Retirar
        btn_depositar = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.ARROW_DOWNWARD, size=32, color=ft.Colors.WHITE),
                    ft.Text("Depositar", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.GREEN_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("depositar"),
            ink=True
        )
        
        btn_retirar = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.ARROW_UPWARD, size=32, color=ft.Colors.WHITE),
                    ft.Text("Retirar", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.BLUE_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("retirar"),
            ink=True
        )
        
        # Fila 2: Transferir y Consultar
        btn_transferir = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.SWAP_HORIZ, size=32, color=ft.Colors.WHITE),
                    ft.Text("Transferir", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.PURPLE_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("transferir"),
            ink=True
        )
        
        btn_consultar = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.ANALYTICS_OUTLINED, size=32, color=ft.Colors.WHITE),
                    ft.Text("Consultar", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.CYAN_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("consultar"),
            ink=True
        )
        
        # Fila 3: Cambiar Clave e Historial
        btn_cambiar_clave = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.LOCK_RESET, size=32, color=ft.Colors.WHITE),
                    ft.Text("Cambiar Clave", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.ORANGE_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("cambiar_clave"),
            ink=True
        )
        
        btn_historial = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.HISTORY, size=32, color=ft.Colors.WHITE),
                    ft.Text("Historial", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=180,
            height=100,
            border_radius=12,
            bgcolor=ft.Colors.INDIGO_700,
            padding=20,
            on_click=lambda e: self.on_ir_vista("historial"),
            ink=True
        )
        
        # Grid de botones
        grid_botones = ft.Column(
            controls=[
                ft.Row(
                    controls=[btn_depositar, btn_retirar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                ft.Row(
                    controls=[btn_transferir, btn_consultar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                ft.Row(
                    controls=[btn_cambiar_clave, btn_historial],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            spacing=20
        )
        
        # ========== BOTÓN CERRAR SESIÓN (CORREGIDO) ==========
        btn_cerrar_sesion = ft.OutlinedButton(
            text="Cerrar sesión",
            icon=ft.Icons.LOGOUT,
            on_click=self.cerrar_sesion,  # CAMBIO: ahora llama a método local
            style=ft.ButtonStyle(
                color=ft.Colors.RED_400,
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(2, ft.Colors.RED_400)
            )
        )
        
        # ========== CONTENEDOR PRINCIPAL ==========
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=20),
                    # Logo
                    ft.Text(
                        "NovaBank",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=30),
                    header,
                    ft.Container(height=40),
                    grid_botones,
                    ft.Container(height=30),
                    btn_cerrar_sesion,
                    ft.Container(height=20)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                scroll=ft.ScrollMode.AUTO
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    "#0a1929",
                    "#1a2332",
                    "#0d3d56",
                    "#114357"
                ]
            ),
            padding=20,
            expand=True
        )
        
        return self.container
    
    def cerrar_sesion(self, e):
        """Método para cerrar sesión"""
        self.on_logout()
    
    def actualizar_saldo(self, nuevo_saldo):
        """Actualiza el saldo mostrado"""
        self.usuario_data["saldo"] = nuevo_saldo
        self.page.update()
