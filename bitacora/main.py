from core import Equipo, Personal, Bitacora

bitacora = Bitacora()

while True:
    print("\n--- MENÚ DE LA BITÁCORA ---")
    print("1. Agregar equipo")
    print("2. Agregar personal")
    print("3. Generar reporte")
    print("4. Ver todo")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        id_equipo = input("ID del equipo: ")
        tipo = input("Tipo: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        estado = input("Estado: ")
        fecha = input("Fecha (dd-mm-aaaa): ")
        equipo = Equipo(id_equipo, tipo, marca, modelo, estado, fecha)
        bitacora.agregar_equipo(equipo)

    elif opcion == "2":
        id_personal = input("ID del personal: ")
        nombre = input("Nombre: ")
        cargo = input("Cargo: ")
        telefono = input("Teléfono: ")
        persona = Personal(id_personal, nombre, cargo, telefono)
        bitacora.agregar_personal(persona)

    elif opcion == "3":
        nombre = input("Nombre del personal que genera el reporte: ")
        id_equipo = input("ID del equipo involucrado: ")
        tipo_accion = input("Tipo de acción (revisión/mantenimiento/etc): ")
        descripcion = input("Descripción del reporte: ")

        # Buscar personal y equipo
        persona = next((p for p in bitacora.personal if p.nombre == nombre), None)
        equipo = next((e for e in bitacora.equipos if e.id_equipo == id_equipo), None)

        if persona and equipo:
            reporte = persona.generar_reporte(equipo, tipo_accion, descripcion)
            bitacora.agregar_reporte(reporte)
        else:
            print("Personal o equipo no encontrados.")

    elif opcion == "4":
        bitacora.listar_todos()

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
