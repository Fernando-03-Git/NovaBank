from database.db_manager import DatabaseManager
from logic.auth import AuthManager

# Probar la base de datos directamente
db = DatabaseManager()
auth = AuthManager()

print("=== PRUEBA DE LOGIN ===\n")

# 1. Ver todos los usuarios en la BD
import sqlite3
conn = sqlite3.connect('database/banco.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT id, nombre, apellido, usuario, saldo FROM usuarios')
usuarios = cursor.fetchall()

print("USUARIOS EN LA BASE DE DATOS:")
for u in usuarios:
    print(f"  ID: {u['id']}, Usuario: {u['usuario']}, Nombre: {u['nombre']} {u['apellido']}, Saldo: ${u['saldo']}")

if not usuarios:
    print("  ⚠️ NO HAY USUARIOS REGISTRADOS\n")
    conn.close()
else:
    print()
    
    # 2. Pedir datos de login
    usuario_input = input("Ingresa el USUARIO para probar login: ")
    clave_input = input("Ingresa la CONTRASEÑA: ")
    
    # 3. Probar login
    print(f"\nProbando login con usuario='{usuario_input}' y clave='{clave_input}'...")
    resultado = auth.iniciar_sesion(usuario_input, clave_input)
    
    print(f"\nResultado del login:")
    print(f"  Éxito: {resultado['exito']}")
    print(f"  Mensaje: {resultado.get('mensaje', 'N/A')}")
    if resultado['exito']:
        print(f"  Usuario logueado: {resultado['usuario']}")
    
    conn.close()

print("\n=== FIN DE LA PRUEBA ===")
