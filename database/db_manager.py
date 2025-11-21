import sqlite3
from datetime import datetime
import hashlib


class DatabaseManager:
    def __init__(self, db_name="database/banco.db"):
        self.db_name = db_name
        self.crear_tablas()
    
    def get_connection(self):
        """Obtiene una conexión a la base de datos"""
        conn = sqlite3.connect(self.db_name, timeout=10.0, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Para acceder a columnas por nombre
        return conn
    
    def crear_tablas(self):
        """Crea las tablas si no existen"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                usuario TEXT UNIQUE NOT NULL,
                clave TEXT NOT NULL,
                saldo REAL DEFAULT 0.0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de transacciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                monto REAL NOT NULL,
                destinatario_id INTEGER,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                descripcion TEXT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                FOREIGN KEY (destinatario_id) REFERENCES usuarios (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def encriptar_clave(self, clave):
        """Encripta la clave usando SHA256"""
        return hashlib.sha256(clave.encode()).hexdigest()
    
    # ========== OPERACIONES DE USUARIOS ==========
    
    def registrar_usuario(self, nombre, apellido, usuario, clave):
        """Registra un nuevo usuario"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            clave_encriptada = self.encriptar_clave(clave)
            
            cursor.execute('''
                INSERT INTO usuarios (nombre, apellido, usuario, clave)
                VALUES (?, ?, ?, ?)
            ''', (nombre, apellido, usuario, clave_encriptada))
            
            conn.commit()
            usuario_id = cursor.lastrowid
            conn.close()
            return {"exito": True, "mensaje": "Usuario registrado exitosamente", "id": usuario_id}
        except sqlite3.IntegrityError:
            return {"exito": False, "mensaje": "El usuario ya existe"}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
    
    def verificar_login(self, usuario, clave):
        """Verifica las credenciales de login"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        clave_encriptada = self.encriptar_clave(clave)
        
        cursor.execute('''
            SELECT * FROM usuarios 
            WHERE usuario = ? AND clave = ?
        ''', (usuario, clave_encriptada))
        
        usuario_data = cursor.fetchone()
        conn.close()
        
        if usuario_data:
            return {
                "exito": True,
                "usuario": {
                    "id": usuario_data["id"],
                    "nombre": usuario_data["nombre"],
                    "apellido": usuario_data["apellido"],
                    "usuario": usuario_data["usuario"],
                    "saldo": usuario_data["saldo"]
                }
            }
        else:
            return {"exito": False, "mensaje": "Usuario o contraseña incorrectos"}
    
    def obtener_usuario_por_id(self, usuario_id):
        """Obtiene la información de un usuario por ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario:
            return {
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "apellido": usuario["apellido"],
                "usuario": usuario["usuario"],
                "saldo": usuario["saldo"]
            }
        return None
    
    def obtener_usuario_por_nombre(self, nombre_usuario):
        """Obtiene un usuario por su nombre de usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (nombre_usuario,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario:
            return {
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "apellido": usuario["apellido"],
                "usuario": usuario["usuario"],
                "saldo": usuario["saldo"]
            }
        return None
    
    def actualizar_saldo(self, usuario_id, nuevo_saldo):
        """Actualiza el saldo de un usuario"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE usuarios 
                SET saldo = ? 
                WHERE id = ?
            ''', (nuevo_saldo, usuario_id))
            
            conn.commit()
        finally:
            if conn:
                conn.close()
    
    def cambiar_clave(self, usuario_id, clave_actual, clave_nueva):
        """Cambia la clave de un usuario"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            clave_actual_encriptada = self.encriptar_clave(clave_actual)
            
            # Verificar que la clave actual sea correcta
            cursor.execute('''
                SELECT id FROM usuarios 
                WHERE id = ? AND clave = ?
            ''', (usuario_id, clave_actual_encriptada))
            
            if cursor.fetchone():
                clave_nueva_encriptada = self.encriptar_clave(clave_nueva)
                cursor.execute('''
                    UPDATE usuarios 
                    SET clave = ? 
                    WHERE id = ?
                ''', (clave_nueva_encriptada, usuario_id))
                conn.commit()
                return {"exito": True, "mensaje": "Clave actualizada exitosamente"}
            else:
                return {"exito": False, "mensaje": "Clave actual incorrecta"}
        finally:
            if conn:
                conn.close()
    
    # ========== OPERACIONES DE TRANSACCIONES ==========
    
    def registrar_transaccion(self, usuario_id, tipo, monto, destinatario_id=None, descripcion=""):
        """Registra una transacción"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO transacciones (usuario_id, tipo, monto, destinatario_id, descripcion)
                VALUES (?, ?, ?, ?, ?)
            ''', (usuario_id, tipo, monto, destinatario_id, descripcion))
            
            conn.commit()
        finally:
            if conn:
                conn.close()
    
    def obtener_transacciones(self, usuario_id, limite=10):
        """Obtiene las últimas transacciones de un usuario"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM transacciones 
            WHERE usuario_id = ? 
            ORDER BY fecha DESC 
            LIMIT ?
        ''', (usuario_id, limite))
        
        transacciones = cursor.fetchall()
        conn.close()
        
        return [{
            "id": t["id"],
            "tipo": t["tipo"],
            "monto": t["monto"],
            "fecha": t["fecha"],
            "descripcion": t["descripcion"],
            "destinatario_id": t["destinatario_id"]
        } for t in transacciones]
