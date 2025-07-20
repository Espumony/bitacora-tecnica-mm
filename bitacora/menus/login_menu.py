""""módulo para manejar el menú de inicio de sesión y autenticación de usuarios."""

from bitacora.models.usuario import Usuario
from bitacora.sql.db import conectar  

def mostrar_login():
    print("🩺 Bienvenido a la Bitácora Médica de Medical Mecánica")
    print("═══════════════════════════════════════════════════════")
    
    username = input("Usuario: ")
    password = input("Contraseña: ")

    con = conectar()
    usuario = Usuario.autenticar(con, username, password)

    if usuario:
        print(f"✅ Acceso concedido, {usuario.username}")
        return usuario
    else:
        print("❌ Acceso denegado. Usuario o contraseña incorrectos.")
        return None
