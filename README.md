<h1 align="center">🏦 NovaBank</h1>

<p align="center">
  <strong>Multiplatform banking app built with Python and Flet</strong><br>
  <sub>Aplicación bancaria multiplataforma desarrollada con Python y Flet</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/Flet-009688?style=for-the-badge&logo=flutter&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

---

## 📖 Descripción

NovaBank es una aplicación bancaria multiplataforma que ofrece una experiencia segura y moderna para la gestión de finanzas personales. Desarrollada con Python y Flet, corre en Android, iOS, web y escritorio adaptándose automáticamente a cada plataforma.

---

## ✨ Características

- Registro e inicio de sesión seguros con hash SHA-256
- Depósitos, retiros y transferencias entre usuarios
- Consulta de saldo en tiempo real
- Historial detallado de transacciones
- Cambio de contraseña
- Interfaz moderna, responsive y multiplataforma
- Persistencia local con SQLite

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| [Python](https://python.org) | Lenguaje principal y lógica de negocio |
| [Flet](https://flet.dev) | Framework multiplataforma sobre Flutter |
| [SQLite](https://www.sqlite.org) | Base de datos local embebida |
| [hashlib](https://docs.python.org/3/library/hashlib.html) | Hash seguro de contraseñas |

---

## 🚀 Instalación y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/Fernando-03-Git/NovaBank.git
cd NovaBank

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python main.py
```

---

## 📁 Estructura del proyecto

```
NovaBank/
├── database/
│   ├── banco.db          # Base de datos SQLite
│   └── db_manager.py     # Gestión de conexiones
├── logic/
│   ├── auth.py           # Autenticación de usuarios
│   ├── transacciones.py  # Lógica de operaciones
│   └── usuario_logic.py  # Gestión de usuarios
├── models/
│   ├── transaccion.py    # Modelo de transacción
│   └── usuario.py        # Modelo de usuario
├── utils/
│   ├── formatters.py     # Formateo de datos
│   └── validators.py     # Validaciones
├── views/
│   ├── login.py          # Pantalla de login
│   ├── dashboard.py      # Panel principal
│   ├── depositar.py      # Vista de depósito
│   ├── retirar.py        # Vista de retiro
│   ├── transferir.py     # Vista de transferencia
│   ├── historial.py      # Historial de movimientos
│   ├── consultar_saldo.py
│   └── cambiar_clave.py
├── main.py               # Punto de entrada
├── requirements.txt
└── .gitignore
```

---

## 🛡️ Seguridad

- Las contraseñas se almacenan con hash SHA-256, nunca en texto plano
- El `.gitignore` excluye la base de datos y archivos sensibles
- No subas archivos `.db` reales ni credenciales a GitHub

---

## 🔮 Próximas funcionalidades

- Dashboard con gráficos de movimientos usando `matplotlib`
- Exportar historial a PDF
- Metas de ahorro con cálculo de intereses
- Sistema de logros por actividad bancaria

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.