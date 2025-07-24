# Menú principal después de iniciar sesión

from bitacora.models.reportes import Reporte
from bitacora.sql.db import conectar

def mostrar_menu_principal(usuario):
    print(f"\n🩺 ¡Hola, {usuario.nombre} ! Bienvenido a la bitácora de Medical Mecánica 💼\n")
    print("Selecciona una opción para continuar:\n")
    print("1. Generar un reporte 📑")
    print("2. Salir 👋")
    print("\n")
    
    opcion = input("Ingresa la opción que deseas realizar:  ")

    try:
        opcion = int(opcion)

        if opcion == 1:
          Reporte.generar_reporte()
           # Esto mandará la función para generar un reporte desde la clase reporte 
        elif opcion == 2:
            print("👋 ¡Hasta luego! Gracias por usar la bitácora de Medical Mecánica.")
            exit()  
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")
            mostrar_menu_principal(usuario)

    except ValueError:
       print("❌ Opción inválida. Por favor, ingresa un número válido.")
       