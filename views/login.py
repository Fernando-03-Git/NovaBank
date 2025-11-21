import flet as ft
from logic.auth import AuthManager


class LoginView:
    def __init__(self, page, on_login_success):
        self.page = page
        self.on_login_success = on_login_success
        self.auth = AuthManager()
        self.container = None
        
    def build(self):
        # ========== CAMPOS DE LOGIN ==========
        self.txt_usuario_login = ft.TextField(
            label="Usuario",
            hint_text="Tu nombre de usuario",
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.BLUE_200,
            focused_border_color=ft.Colors.BLUE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.BLUE_400,
            prefix_icon=ft.Icons.PERSON_OUTLINE
        )
        
        self.txt_clave_login = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.BLUE_200,
            focused_border_color=ft.Colors.BLUE_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.BLUE_400,
            prefix_icon=ft.Icons.LOCK_OUTLINE
        )
        
        self.btn_login = ft.ElevatedButton(
            text="Iniciar sesión",
            width=350,
            height=50,
            on_click=self.hacer_login,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_600,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4
            )
        )
        
        # ========== CAMPOS DE REGISTRO ==========
        self.txt_nombre_registro = ft.TextField(
            label="Nombre",
            hint_text="Tu nombre",
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.CYAN_200,
            focused_border_color=ft.Colors.CYAN_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.CYAN_400,
            prefix_icon=ft.Icons.BADGE_OUTLINED
        )
        
        self.txt_apellido_registro = ft.TextField(
            label="Apellido",
            hint_text="Tu apellido",
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.CYAN_200,
            focused_border_color=ft.Colors.CYAN_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.CYAN_400,
            prefix_icon=ft.Icons.BADGE_OUTLINED
        )
        
        self.txt_usuario_registro = ft.TextField(
            label="Usuario",
            hint_text="Elige un nombre de usuario",
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.CYAN_200,
            focused_border_color=ft.Colors.CYAN_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.CYAN_400,
            prefix_icon=ft.Icons.PERSON_ADD_OUTLINED
        )
        
        self.txt_clave_registro = ft.TextField(
            label="Contraseña",
            hint_text="Mínimo 4 caracteres",
            password=True,
            can_reveal_password=True,
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.CYAN_200,
            focused_border_color=ft.Colors.CYAN_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.CYAN_400,
            prefix_icon=ft.Icons.LOCK_OPEN_OUTLINED
        )
        
        self.txt_confirmar_clave = ft.TextField(
            label="Confirmar contraseña",
            hint_text="Repite tu contraseña",
            password=True,
            can_reveal_password=True,
            width=350,
            height=60,
            text_size=14,
            border_radius=12,
            border_color=ft.Colors.CYAN_200,
            focused_border_color=ft.Colors.CYAN_400,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            cursor_color=ft.Colors.CYAN_400,
            prefix_icon=ft.Icons.LOCK_OUTLINED
        )
        
        self.btn_registro = ft.ElevatedButton(
            text="Crear cuenta",
            width=350,
            height=50,
            on_click=self.hacer_registro,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.CYAN_600,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4
            )
        )
        
        # ========== MENSAJE DE ERROR/ÉXITO ==========
        self.txt_mensaje = ft.Container(
            content=ft.Text(
                value="",
                size=13,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.W_500
            ),
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.RED),
            padding=12,
            border_radius=10,
            visible=False
        )
        
        # ========== CONTENEDOR LOGIN ==========
        self.container_login = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Iniciar sesión",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Container(height=30),
                    self.txt_usuario_login,
                    ft.Container(height=15),
                    self.txt_clave_login,
                    ft.Container(height=25),
                    self.btn_login
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            ),
            padding=40,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
            width=450,
            visible=True
        )
        
        # ========== CONTENEDOR REGISTRO ==========
        self.container_registro = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Crear cuenta",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    ),
                    ft.Container(height=25),
                    self.txt_nombre_registro,
                    ft.Container(height=15),
                    self.txt_apellido_registro,
                    ft.Container(height=15),
                    self.txt_usuario_registro,
                    ft.Container(height=15),
                    self.txt_clave_registro,
                    ft.Container(height=15),
                    self.txt_confirmar_clave,
                    ft.Container(height=25),
                    self.btn_registro
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                scroll=ft.ScrollMode.AUTO
            ),
            padding=40,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
            width=450,
            visible=False
        )
        
        # ========== TABS PARA CAMBIAR ENTRE LOGIN Y REGISTRO ==========
        self.btn_tab_login = ft.Container(
            content=ft.Text(
                "Iniciar sesión",
                size=15,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            padding=ft.padding.symmetric(horizontal=35, vertical=14),
            border_radius=12,
            bgcolor=ft.Colors.BLUE_700,
            on_click=self.cambiar_a_login,
            ink=True
        )
        
        self.btn_tab_registro = ft.Container(
            content=ft.Text(
                "Crear cuenta",
                size=15,
                weight=ft.FontWeight.NORMAL,
                color=ft.Colors.GREY_400
            ),
            padding=ft.padding.symmetric(horizontal=35, vertical=14),
            border_radius=12,
            bgcolor=ft.Colors.TRANSPARENT,
            on_click=self.cambiar_a_registro,
            ink=True
        )
        
        tabs_row = ft.Row(
            controls=[self.btn_tab_login, self.btn_tab_registro],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        # ========== HEADER CON LOGO ==========
        header = ft.Column(
            controls=[
                ft.Text(
                    "NovaBank",
                    size=52,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),
                ft.Text(
                    "Seguro • Rápido • Moderno",
                    size=15,
                    color=ft.Colors.CYAN_300,
                    weight=ft.FontWeight.W_500
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8
        )
        
        # ========== CONTENEDOR PRINCIPAL ==========
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=35),
                    header,
                    ft.Container(height=45),
                    ft.Text(
                        "Bienvenido de nuevo",
                        size=34,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Accede a tu cuenta o crea una nueva para continuar",
                        size=14,
                        color=ft.Colors.GREY_300,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=35),
                    tabs_row,
                    ft.Container(height=25),
                    self.txt_mensaje,
                    ft.Stack(
                        controls=[
                            self.container_login,
                            self.container_registro
                        ]
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                scroll=ft.ScrollMode.AUTO
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    "#0a1929",  # Azul oscuro profundo
                    "#1a2332",  # Azul grisáceo oscuro
                    "#0d3d56",  # Azul petróleo oscuro
                    "#114357"   # Azul verdoso oscuro
                ]
            ),
            padding=20,
            expand=True
        )
        
        return self.container
    
    def cambiar_a_login(self, e):
        """Cambia a la vista de login"""
        self.container_login.visible = True
        self.container_registro.visible = False
        self.btn_tab_login.bgcolor = ft.Colors.BLUE_700
        self.btn_tab_login.content.color = ft.Colors.WHITE
        self.btn_tab_login.content.weight = ft.FontWeight.BOLD
        self.btn_tab_registro.bgcolor = ft.Colors.TRANSPARENT
        self.btn_tab_registro.content.color = ft.Colors.GREY_400
        self.btn_tab_registro.content.weight = ft.FontWeight.NORMAL
        self.txt_mensaje.visible = False
        self.limpiar_campos()
        self.page.update()
    
    def cambiar_a_registro(self, e):
        """Cambia a la vista de registro"""
        self.container_login.visible = False
        self.container_registro.visible = True
        self.btn_tab_login.bgcolor = ft.Colors.TRANSPARENT
        self.btn_tab_login.content.color = ft.Colors.GREY_400
        self.btn_tab_login.content.weight = ft.FontWeight.NORMAL
        self.btn_tab_registro.bgcolor = ft.Colors.CYAN_700
        self.btn_tab_registro.content.color = ft.Colors.WHITE
        self.btn_tab_registro.content.weight = ft.FontWeight.BOLD
        self.txt_mensaje.visible = False
        self.limpiar_campos()
        self.page.update()
    
    def limpiar_campos(self):
        """Limpia todos los campos"""
        self.txt_usuario_login.value = ""
        self.txt_clave_login.value = ""
        self.txt_nombre_registro.value = ""
        self.txt_apellido_registro.value = ""
        self.txt_usuario_registro.value = ""
        self.txt_clave_registro.value = ""
        self.txt_confirmar_clave.value = ""
    
    def hacer_login(self, e):
        """Maneja el evento de login"""
        usuario = self.txt_usuario_login.value
        clave = self.txt_clave_login.value
        
        if not usuario or not clave:
            self.mostrar_mensaje("Por favor completa todos los campos", ft.Colors.RED)
            return
        
        resultado = self.auth.iniciar_sesion(usuario, clave)
        
        if resultado["exito"]:
            self.on_login_success(resultado["usuario"])
        else:
            self.mostrar_mensaje(resultado["mensaje"], ft.Colors.RED)
    
    def hacer_registro(self, e):
        """Maneja el evento de registro"""
        nombre = self.txt_nombre_registro.value.strip()
        apellido = self.txt_apellido_registro.value.strip()
        usuario = self.txt_usuario_registro.value.strip()
        clave = self.txt_clave_registro.value.strip()
        confirmar = self.txt_confirmar_clave.value.strip()
        
        if not nombre or not apellido or not usuario or not clave or not confirmar:
            self.mostrar_mensaje("Por favor completa todos los campos", ft.Colors.RED)
            return
        
        if clave != confirmar:
            self.mostrar_mensaje("Las contraseñas no coinciden", ft.Colors.RED)
            return
        
        if len(clave) < 4:
            self.mostrar_mensaje("La contraseña debe tener al menos 4 caracteres", ft.Colors.RED)
            return
        
        resultado = self.auth.registrar_usuario(nombre, apellido, usuario, clave)
        
        if resultado["exito"]:
            self.mostrar_mensaje("¡Usuario registrado! Ahora puedes iniciar sesión", ft.Colors.GREEN)
            self.limpiar_campos()
        else:
            self.mostrar_mensaje(resultado["mensaje"], ft.Colors.RED)
    
    def mostrar_mensaje(self, mensaje, color):
        """Muestra un mensaje en pantalla"""
        self.txt_mensaje.content.value = mensaje
        self.txt_mensaje.content.color = ft.Colors.WHITE
        self.txt_mensaje.bgcolor = ft.Colors.with_opacity(0.9, color)
        self.txt_mensaje.visible = True
        self.page.update()
