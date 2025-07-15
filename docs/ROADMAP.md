# Roadmap · Bitácora Técnica MM


## Contexto
Se ha rediseñado el proyecto `bitacora` para adoptar un enfoque completamente orientado a objetos (POO). Las clases clave son: `Personal`, `Equipo`, `Reporte` y `Bitacora`.

Este rediseño busca mayor escalabilidad, mantenibilidad y claridad en la lógica de negocio.

---

## 🎯 OBJETIVOS DE LA SEMANA (3 IMPLEMENTACIONES CLAVE)

### ✅ 1. Implementar clase `Equipo`
- Atributos: `id_equipo`, `nombre`, `marca`, `modelo`, `estado`, `ubicacion`
- Métodos esperados: `cambiar_estado()`, `actualizar_ubicacion()`, `mostrar_info()`
- Integración: debe ser compatible con `Reporte`

### ✅ 2. Implementar clase `Bitacora`
- Debe almacenar todos los reportes generados
- Métodos:
  - `agregar_reporte(reporte)`
  - `buscar_por_tecnico(nombre)`
  - `buscar_por_equipo(id_equipo)`
  - `listar_todos()`
- Posible exportación a CSV/JSON (plan futuro)

### ✅ 3. Crear flujo de prueba básico
- Crear 1 equipo, 1 persona
- Generar al menos 2 reportes distintos (preventivo y correctivo)
- Agregarlos a la bitácora
- Consultar bitácora por técnico y por equipo
- Imprimir resultados con `.mostrar_informacion()` para validar

---

## 🔄 Pendientes futuros (para próximas semanas)

- Persistencia de datos: guardar/leer desde archivo (JSON o CSV)
- Interfaz de línea de comandos o menú de consola
- Validaciones de datos (tipos de acción, formato de entrada)
- Soporte para múltiples sedes/hospitales

---

## 🗓️ Última actualización
*2025-07-15*

