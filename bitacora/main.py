from core import Equipo, Personal, Bitacora  # Importamos tus clases

# PASO 1: Crear un equipo
equipo1 = Equipo(
    id_equipo="EQ001",
    tipo="Monitor",
    marca="Philips",
    modelo="MX450",
    estado="activo",
    fecha="2025-07-15"
)

# PASO 2: Crear un técnico (objeto Personal)
tecnico1 = Personal(
    id_personal="P001",
    nombre="Erick Peña",
    cargo="Técnico Biomédico",
    telefono="555-123-4567"
)

# PASO 3: Crear una bitácora para guardar reportes
bitacora = Bitacora()

# PASO 4: El técnico genera un reporte
reporte = tecnico1.generar_reporte(
    equipo=equipo1,
    tipo_accion="mantenimiento preventivo",
    descripcion="Limpieza y prueba de alarmas. Todo OK."
)

# PASO 5: Guardar el reporte en la bitácora
bitacora.reportes.append(reporte)

# PASO 6: Mostrar los reportes
print("📄 Reportes en la bitácora:")
for rep in bitacora.listar_todos():
    print(rep.mostrar_informacion())
