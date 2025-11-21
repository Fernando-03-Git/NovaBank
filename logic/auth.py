import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_manager import DatabaseManager


class AuthManager:
    def __init__(self):
        self.db = DatabaseManager()
    
    def registrar_usuario(self, nombre, apellido, usuario, clave):
        """
        Registra un nuevo usuario en el sistema
        
        Args:
            nombre: Nombre del usuario
            apellido: Apellido del usuario
            usuario: Nombre de usuario (único)
            clave: Contraseña
            
        Returns:
            dict: {"exito": bool, "mensaje": str, "usuario": dict}
        """
        # Validaciones
        if not nombre or not apellido or not usuario or not clave:
            return {
                "exito": False,
                "mensaje": "Todos los campos son obligatorios"
            }
        
        if len(usuario) < 3:
            return {
                "exito": False,
                "mensaje": "El usuario debe tener al menos 3 caracteres"
            }
        
        if len(clave) < 4:
            return {
                "exito": False,
                "mensaje": "La contraseña debe tener al menos 4 caracteres"
            }
        
        # Intentar registrar en la base de datos
        resultado = self.db.registrar_usuario(nombre, apellido, usuario, clave)
        
        if resultado["exito"]:
            # Obtener los datos completos del usuario recién creado
            usuario_data = self.db.obtener_usuario_por_id(resultado["id"])
            return {
                "exito": True,
                "mensaje": "Usuario registrado exitosamente",
                "usuario": usuario_data
            }
        else:
            return resultado
    
    def iniciar_sesion(self, usuario, clave):
        """
        Inicia sesión con las credenciales proporcionadas
        
        Args:
            usuario: Nombre de usuario
            clave: Contraseña
            
        Returns:
            dict: {"exito": bool, "mensaje": str, "usuario": dict}
        """
        # Validaciones
        if not usuario or not clave:
            return {
                "exito": False,
                "mensaje": "Usuario y contraseña son obligatorios"
            }
        
        # Verificar credenciales
        resultado = self.db.verificar_login(usuario, clave)
        
        if resultado["exito"]:
            return {
                "exito": True,
                "mensaje": "Inicio de sesión exitoso",
                "usuario": resultado["usuario"]
            }
        else:
            return {
                "exito": False,
                "mensaje": "Usuario o contraseña incorrectos"
            }
    
    def verificar_usuario_existe(self, usuario):
        """
        Verifica si un nombre de usuario ya existe
        
        Args:
            usuario: Nombre de usuario a verificar
            
        Returns:
            bool: True si existe, False si no
        """
        usuario_data = self.db.obtener_usuario_por_nombre(usuario)
        return usuario_data is not None
