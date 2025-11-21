# 🚀 NovaBank

**Gestión bancaria moderna, segura y multiplataforma con Python y Flet**

---

## 📖 Descripción

NovaBank es una aplicación bancaria multiplataforma desarrollada con Python y Flet que ofrece a los usuarios una experiencia segura, eficiente y moderna para la gestión de sus finanzas. Permite: depósitos, retiros, transferencias entre cuentas, consulta de saldos, gestión de contraseñas y visualización de historial de transacciones. NovaBank está diseñada para funcionar en Android, iOS, web y escritorio, adaptándose automáticamente a cada plataforma.

---

## ✨ Características

- Registro e inicio de sesión seguros con hash SHA-256
- Depósitos, retiros y transferencias entre usuarios
- Consulta de saldo en tiempo real
- Historial detallado de transacciones
- Cambio de contraseña
- Interfaz gráfica moderna, responsive y amigable
- Persistencia local con SQLite
- Código Python limpio, modular y documentado
- Compilación fácil a APK con Flet CLI

---

## 🛠️ Tecnologías y frameworks

- **[Flet](https://flet.dev):** Para crear aplicaciones multiplataforma con Python, renderizando las interfaces con Flutter.
- **[Python](https://python.org):** Lenguaje principal del backend y la lógica del negocio.
- **[Flutter](https://flutter.dev):** Motor gráfico sobre el que Flet renderiza la interfaz de usuario.
- **[SQLite](https://www.sqlite.org):** Base de datos local, embebida y eficiente.
- **[hashlib](https://docs.python.org/3/library/hashlib.html):** Módulo estándar para el hash de contraseñas.

---

## 🧭 Uso

1. **Pantalla de inicio de sesión y registro**
 - Completa el registro para un usuario nuevo o inicia sesión si ya tienes cuenta.
2. **Dashboard**
 - Visualiza tu saldo y navega entre las distintas opciones.
3. **Operaciones disponibles**
 - Deposita, retira, transfiere fondos y consulta tu historial.
4. **Gestión de seguridad**
 - Cambia tu contraseña en cualquier momento desde la aplicación.

---

## 🛡️ Notas de seguridad

- **No subas archivos de base de datos reales ni contraseñas a GitHub.**
- El archivo `.gitignore` ya omite carpetas y archivos sensibles.
- Las contraseñas se almacenan con hash seguro (SHA-256), nunca en texto plano.

---

## 🚀 Planes a futuro

NovaBank está pensada para seguir evolucionando. Algunas de las ideas y funcionalidades que podrían añadirse en próximas versiones son:

- **Logros y medallas por actividad bancaria:** Un sistema de gamificación para motivar el uso responsable, recompensar buenas prácticas financieras y fomentar el ahorro.
- **Mensajes personalizados en consulta de saldo y transferencias:** Reacciones contextuales, consejos o motivaciones automáticas basadas en los hábitos del usuario.
- **Intereses automáticos y metas de ahorro:** Posibilidad de definir objetivos de ahorro y cálculo automático de intereses al alcanzar metas, promoviendo la educación financiera.
- **Dashboard con gráficos y visualizaciones:** Integración de matplotlib o plotly para proveer análisis visual de movimientos y gastos, permitiendo tomar mejores decisiones.
- **Mini IA financiera:** Un sistema que sugiera acciones de ahorro o inversión según el historial y perfil de cada usuario.
- **Control por voz:** Realizar operaciones simples y consultas mediante comandos orales, aumentando la accesibilidad.
- **Exportar reportes a PDF:** Descargar resúmenes de movimientos o historial como archivos PDF para facilitar trámites y registros.

Estas ideas están alineadas con las tendencias de la banca digital moderna, enfocadas en la personalización, accesibilidad y educación financiera de los usuarios.
