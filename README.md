# Login Interactivo Tkinter

Una interfaz gráfica de usuario (GUI) limpia y moderna desarrollada en Python utilizando **Tkinter** para gestionar el control de acceso. El sistema valida las credenciales de forma segura utilizando variables de entorno y cuenta con controles interactivos para mejorar la experiencia del usuario.

## 🚀 Características
*   **Validación Segura:** Lee el usuario y la contraseña desde un archivo `.env` externo para proteger datos sensibles.
*   **Interfaz Dinámica:** Mensajes de alerta en tiempo real con colores según el estado (Éxito, Error o Advertencia).
*   **Atajos de Teclado:** Permite iniciar sesión presionando directamente la tecla `Enter`.
*   **Seguridad Visual:** Incluye un botón interactivo con un icono de ojo para alternar la visibilidad de la contraseña (`Mostrar` / `Ocultar`).
*   **Control de Flujo:** Botón dedicado para limpiar campos automáticamente y reubicar el cursor de escritura.

## 🛠️ Tecnologías utilizadas
*   **Python 3.x**
*   **Tkinter** (Librería nativa para interfaces gráficas)
*   **python-dotenv** (Gestión de variables de entorno)

## 📦 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el proyecto
```bash
git clone https://github.com
cd TU_REPOSITORIO
```

### 2. Instalar dependencias
Este proyecto requiere el paquete `python-dotenv`. Instálalo ejecutando:
```bash
pip install python-dotenv
```

### 3. Configurar las variables de entorno
Crea un archivo llamado `.env` en la raíz principal del proyecto y define tus credenciales de acceso de la siguiente manera:
```env
APP_USER=mi_usuario_seguro
APP_PASSWORD=mi_contraseña_secreta
```

## 💻 Uso

Para arrancar la interfaz gráfica de inicio de sesión, ejecuta el script principal:

```bash
python nombre_de_tu_archivo.py
```