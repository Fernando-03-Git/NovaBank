import flet as ft
from views.login import LoginView
from views.dashboard import DashboardView
from views.depositar import DepositarView
from views.retirar import RetirarView
from views.transferir import TransferirView
from views.consultar_saldo import ConsultarSaldoView
from views.cambiar_clave import CambiarClaveView
from views.historial import HistorialView


def main(page: ft.Page):
    page.title = "NovaBank"
    
    # CAMBIOS PARA MÓVIL: Responsive
    page.window.width = 400  # Ancho móvil
    page.window.height = 800  # Alto móvil
    page.window.resizable = True  # Permitir redimensionar
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0  # Sin padding para aprovechar pantalla
    page.scroll = ft.ScrollMode.AUTO  # Scroll automático
    
    usuario_actual = None
    
    def on_login_success(usuario_data):
        nonlocal usuario_actual
        usuario_actual = usuario_data
        mostrar_dashboard()
    
    def mostrar_login():
        page.controls.clear()
        login_view = LoginView(page, on_login_success)
        page.add(login_view.build())
        page.update()
    
    def mostrar_dashboard():
        page.controls.clear()
        dashboard_view = DashboardView(page, usuario_actual, on_logout, on_ir_vista)
        page.add(dashboard_view.build())
        page.update()
    
    def mostrar_depositar():
        page.controls.clear()
        depositar_view = DepositarView(page, usuario_actual, volver_dashboard)
        page.add(depositar_view.build())
        page.update()
    
    def mostrar_retirar():
        page.controls.clear()
        retirar_view = RetirarView(page, usuario_actual, volver_dashboard)
        page.add(retirar_view.build())
        page.update()
    
    def mostrar_transferir():
        page.controls.clear()
        transferir_view = TransferirView(page, usuario_actual, volver_dashboard)
        page.add(transferir_view.build())
        page.update()
    
    def mostrar_consultar():
        page.controls.clear()
        consultar_view = ConsultarSaldoView(page, usuario_actual, volver_dashboard)
        page.add(consultar_view.build())
        page.update()
    
    def mostrar_cambiar_clave():
        page.controls.clear()
        cambiar_view = CambiarClaveView(page, usuario_actual, volver_dashboard)
        page.add(cambiar_view.build())
        page.update()
    
    def mostrar_historial():
        page.controls.clear()
        historial_view = HistorialView(page, usuario_actual, volver_dashboard)
        page.add(historial_view.build())
        page.update()
    
    def volver_dashboard(usuario_data_actualizado):
        nonlocal usuario_actual
        usuario_actual = usuario_data_actualizado
        mostrar_dashboard()
    
    def on_ir_vista(nombre_vista):
        if nombre_vista == "depositar":
            mostrar_depositar()
        elif nombre_vista == "retirar":
            mostrar_retirar()
        elif nombre_vista == "transferir":
            mostrar_transferir()
        elif nombre_vista == "consultar":
            mostrar_consultar()
        elif nombre_vista == "cambiar_clave":
            mostrar_cambiar_clave()
        elif nombre_vista == "historial":
            mostrar_historial()
    
    def on_logout():
        nonlocal usuario_actual
        usuario_actual = None
        mostrar_login()
    
    mostrar_login()


if __name__ == "__main__":
    ft.app(target=main)
