import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox

# Cargar las variables de entorno
load_dotenv()

USER_CORRECTO = os.getenv("APP_USER")
PASSWORD_CORRECTA = os.getenv("APP_PASSWORD")

# Función para verificar las credenciales
def verificar(event=None): # 'event=None' permite que funcione con el botón y con la tecla Enter
    usuario_ingresado = entrada_usuario.get().strip()
    contrasena_ingresada = entrada_contra.get().strip()
    
    # Validar campos vacíos
    if not usuario_ingresado or not contrasena_ingresada:
        resultado.config(text="⚠ Por favor, rellena todos los campos", fg="#E67E22")
        return

    if usuario_ingresado == USER_CORRECTO and contrasena_ingresada == PASSWORD_CORRECTA:
        resultado.config(text="✅ Acceso correcto. ¡Bienvenido!", fg="#2ECC71")
        # Ventana emergente interactiva de éxito
        messagebox.showinfo("Éxito", f"¡Bienvenido de nuevo, {usuario_ingresado}!")
    else:
        resultado.config(text="❌ Usuario o contraseña incorrectos", fg="#E74C3C")

# Función para limpiar el formulario
def limpiar_campos():
    entrada_usuario.delete(0, tk.END)
    entrada_contra.delete(0, tk.END)
    resultado.config(text="")
    entrada_usuario.focus() # Pone el cursor de nuevo en el primer campo

# Función para mostrar u ocultar el texto de la contraseña
def alternar_contrasena():
    if entrada_contra.cget('show') == '*':
        entrada_contra.config(show='')
        btn_mostrar.config(text="👁 Ocultar")
    else:
        entrada_contra.config(show='*')
        btn_mostrar.config(text="👁 Mostrar")

# --- Configuración de la Interfaz Estilizada ---
ventana = tk.Tk()
ventana.title("Login Interactivo")
ventana.geometry("400x380")
ventana.configure(bg="#F5F6FA") # Color de fondo suave

# Vincular la tecla ENTER de tu teclado para verificar directamente
ventana.bind('<Return>', verificar)

# Título de bienvenida
tk.Label(ventana, text="🔑 Control de Acceso", font=("Arial", 16, "bold"), bg="#F5F6FA", fg="#2C3E50").pack(pady=15)

# Contenedor de Usuario
tk.Label(ventana, text="Usuario:", font=("Arial", 10), bg="#F5F6FA", fg="#7F8C8D").pack(anchor="w", padx=50)
entrada_usuario = tk.Entry(ventana, font=("Arial", 11), bd=2, relief="groove")
entrada_usuario.pack(fill="x", padx=50, pady=5)
entrada_usuario.focus()

# Contenedor de Contraseña
tk.Label(ventana, text="Contraseña:", font=("Arial", 10), bg="#F5F6FA", fg="#7F8C8D").pack(anchor="w", padx=50)
frame_pas = tk.Frame(ventana, bg="#F5F6FA") # Frame para alinear campo y botón de ojo
frame_pas.pack(fill="x", padx=50, pady=5)

entrada_contra = tk.Entry(frame_pas, show="*", font=("Arial", 11), bd=2, relief="groove")
entrada_contra.pack(side="left", expand=True, fill="x")

# Botón interactivo dentro del campo para ver la contraseña
btn_mostrar = tk.Button(frame_pas, text="👁 Mostrar", font=("Arial", 8), command=alternar_contrasena, bg="#DCDDE1", relief="flat")
btn_mostrar.pack(side="right", padx=5)

# --- Fila Interactiva de Botones Principales ---
frame_botones = tk.Frame(ventana, bg="#F5F6FA")
frame_botones.pack(pady=20)

btn_verificar = tk.Button(frame_botones, text="🚀 Verificar", font=("Arial", 10, "bold"), bg="#44BD32", fg="white", width=12, command=verificar, relief="raised", bd=3)
btn_verificar.pack(side="left", padx=10)

btn_limpiar = tk.Button(frame_botones, text="🧹 Limpiar", font=("Arial", 10), bg="#718093", fg="white", width=12, command=limpiar_campos, relief="raised", bd=3)
btn_limpiar.pack(side="right", padx=10)

# Mensaje dinámico de resultado
resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"), bg="#F5F6FA")
resultado.pack(pady=10)

ventana.mainloop()