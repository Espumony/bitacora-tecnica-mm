# Bitácora de Desarrollo

## 2025-07-14
- Arranqué sistema de documentación.
- Pendiente: implementar `agregar_entrada()` con escritura en JSON.

## 2025-07-15
- Se cambió todo el proyecto para migrarlo a un diseño más orientado a clases.
- Se crearon clases Equipo, Personal, Reporte y Bitacora

## 2025-07-16
- Se implementó correctamente la persistencia de datos en JSON desde la clase Bitacora.
- Ahora es posible agregar instancias de Equipo, Personal y Reporte, las cuales se guardan automáticamente al archivo bitacora.json.
- Se solucionó un bug donde agregar_equipo() no era reconocido, probablemente por conflicto de caché o mal refresco del editor.
- Se consolidó el flujo básico entre core.py y main.py.

## 2025-07-20
-Cambié de nuevo el proyecto por completo, ahora guardo en una base de datos sqlite en lugar de archivos json.
-Realicé la conexión y autenticación para utilizar la app.
-Se rehizo desde cero la estructura del proyecto.