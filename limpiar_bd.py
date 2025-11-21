import os
import sqlite3

print("=" * 50)
print("  LIMPIAR BASE DE DATOS - BANCO APP")
print("=" * 50)

db_path = 'database/banco.db'

# Verificar si existe
if not os.path.exists(db_path):
    print("\n⚠️  No existe base de datos para limpiar")
    print(f"   Ruta buscada: {db_path}")
else:
    # Mostrar usuarios actuales
    print("\n📊 USUARIOS ACTUALES EN LA BASE DE DATOS:")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) as total FROM usuarios')
    total = cursor.fetchone()['total']
    
    if total == 0:
        print("   ✓ La base de datos ya está vacía")
    else:
        print(f"   Total de usuarios: {total}\n")
        cursor.execute('SELECT id, usuario, nombre, apellido FROM usuarios')
        for u in cursor.fetchall():
            print(f"   - ID {u['id']}: {u['usuario']} ({u['nombre']} {u['apellido']})")
    
    conn.close()
    
    # Confirmar eliminación
    print("\n⚠️  ADVERTENCIA: Esto eliminará TODOS los datos")
    confirmacion = input("\n¿Estás seguro? (escribe 'SI' para confirmar): ")
    
    if confirmacion.upper() == 'SI':
        print("\n🗑️  Eliminando base de datos...")
        os.remove(db_path)
        print("✅ Base de datos eliminada exitosamente")
        print("\n💡 La próxima vez que ejecutes la app, se creará")
        print("   una base de datos nueva y vacía")
    else:
        print("\n❌ Operación cancelada")

print("\n" + "=" * 50)
