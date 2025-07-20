"""Punto de entrada del programa. Aquí se invoca el menú y las funciones principales."""


from bitacora.sql.db import crear_tablas
from bitacora.menus.login_menu import mostrar_login
from bitacora.menus.main_menu import mostrar_menu_principal

def main():
    crear_tablas()
    usuario = mostrar_login()
    if usuario:
        print(f"🎉 Sesión iniciada con {usuario.username}")
        mostrar_menu_principal(usuario)
    else:
        print("Cerrando aplicación...")

if __name__ == "__main__":
    main()