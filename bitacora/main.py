"""Punto de entrada del programa. Aquí se invoca el menú y las funciones principales."""


from bitacora.sql.db import crear_tablas
from bitacora.menus.login_menu import mostrar_login

if __name__ == "__main__":
    crear_tablas()
    usuario = mostrar_login()
    if usuario:
        print(f"🎉 Sesión iniciada con {usuario.username}")
    else:
        print("Cerrando aplicación...")
