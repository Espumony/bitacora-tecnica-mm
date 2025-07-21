# Menú principal después de iniciar sesión

def mostrar_menu_principal(usuario):
    print(f"\n🩺 ¡Hola, {usuario.username}! Bienvenido a la bitácora de Medical Mecánica 💼\n")
    print("Selecciona una opción para continuar:\n")
    print("1. Agregar un equipo")
    print("\n")
    
    opcion = input("Ingresa la opción que deseas realizar:  ")

    try:
        opcion = int(opcion)

        if opcion == "1":
          pass # Esto mandará la función para agregar equipos desde la clase Equipo, agregar_equipo() es un método de la calse Equipo 
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")
            mostrar_menu_principal(usuario)

    except ValueError:
       print("❌ Opción inválida. Por favor, ingresa un número válido.")
       