#bitacora/core.py

import sys

print ("\n Acta Médica #001 – Respiración Asistida del Sistema \n")

def mostrar_menu():
    """Muestra el menu"principal de opciones."""
    while True:
        print("\n=== Menú ===\n")
        for i, (opcion, _) in enumerate(acciones, 1):
            print(f"{i}. {opcion}")
        print("\n")
        try:
            eleccion = int(input("Seleccione una opción: "))
            accion = menu.get(eleccion)
            if accion:
                accion()
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def agregar_entrada():
    """Agrega una nueva entrada a la bitácora."""
    

def editar_entrada():
    """Edita una entrada existente en la bitácora."""
    pass

def listar_entradas():
    """Muestra todas las entrAdas registradas."""
    pass

def exportar_entradas():
    """Exporta las entradas a un archivo externo."""
    pass

def salir():
    """Finaliza el programa."""
    print("Saliendo del programa...")
    sys.exit()

acciones = [("Agregar Entrada", agregar_entrada),
        ("Listar entradas", listar_entradas),
        ("Editar entradas", editar_entrada),
        ("Exportar entradas", exportar_entradas),
        ("Salir", salir)] # Lista de opciones del menú

menu = {i: func for i, (_, func) in enumerate(acciones, 1)}

equipos = []

def main():
    """Función principal que ejecuta el programa."""
   
    mostrar_menu()


main()
