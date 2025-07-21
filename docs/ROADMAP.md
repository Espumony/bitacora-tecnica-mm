# Roadmap · Bitácora Técnica MM

# 🧭 Roadmap Peña: Sistema de Reportes Técnicos

## 🟢 FASE 1: Lo que ya tienes (¡y no hay que tocar!)
⏱ Tiempo espiritual: *Hecho con amor y sudor de coder*
- [✅] Estructura modular del proyecto lista.
- [✅] Clases de `Usuario`, `Equipo`, y `Reporte` separadas.
- [✅] Conexión a base de datos SQLite funcional.
- [✅] Almacenamiento de usuarios (sin hashear, sistema cerrado).
- [✅] Sesión por consola, sin interfaz gráfica.
- [✅] Lógica de persistencia básica funcionando.

---

## 🔵 FASE 2: Definición de base de datos y relaciones
⏱ Tiempo espiritual: *Una sentada de concentración + unos dibujos con cafecito*

**Objetivos:**
- [ ] Diseñar bien las relaciones entre `usuarios`, `equipos` y `reportes`.
- [ ] Decidir claves primarias y foráneas.
- [ ] Asegurar integridad referencial mínima.

**Notas clave:**
- `reportes` → debe tener `usuario_id` y `equipo_id`.
- `equipos` → debe tener campos modificables según el tipo de reporte (estado, fecha de última intervención, etc).
- `usuarios` → si no vas a tener muchos, mantenlo simple.

---

## 🟡 FASE 3: Lógica de sesión ligada a reportes
⏱ Tiempo espiritual: *Una tarde intensa de código y pruebas*

**Objetivos:**
- [ ] Al iniciar sesión, guardar al usuario activo (estructura global o archivo temporal).
- [ ] Al generar un reporte, asociar automáticamente el `usuario_id` del logueado.
- [ ] Validar que no se pueda hacer nada sin sesión iniciada.

---

## 🟣 FASE 4: Generación de reportes funcionales
⏱ Tiempo espiritual: *Varias sesiones dedicadas, pero cada una es satisfactoria*

**Objetivos:**
- [ ] Crear funciones específicas por tipo de reporte:  
  - Instalación → crea un nuevo equipo.  
  - Mantenimiento → actualiza campos del equipo.  
  - Falla → cambia estado a "en falla".  
  - Retiro → oculta el equipo (soft delete).  
- [ ] Hacer inmutables los reportes: una vez guardado, no se toca.
- [ ] Validaciones mínimas para evitar campos vacíos, tipos incorrectos, etc.

---

## 🟤 FASE 5: Validaciones y control de errores
⏱ Tiempo espiritual: *Una semana de "descubrir errores que no sabías que existían"*

**Objetivos:**
- [ ] Determinar campos obligatorios por tipo de reporte.
- [ ] Validar entradas desde consola para evitar errores de tipeo.
- [ ] Manejar errores de guardado (`try/except` al guardar en DB).
- [ ] Dar retroalimentación clara si algo falla.

**Extra espiritual:**  
Implementar un mini “formulario de consola” donde si el usuario escribe mal un campo, pueda reintentarlo sin perder todo lo anterior.

---

## 🔘 FASE 6: Búsquedas y consultas
⏱ Tiempo espiritual: *Una buena semana, pero se disfruta ver los resultados*

**Objetivos:**
- [ ] Consultar reportes por:  
  - Fecha  
  - Usuario  
  - Equipo  
  - Tipo de reporte  
- [ ] Consultar estado actual de un equipo (último mantenimiento, si está en falla, etc.).
- [ ] Dejar espacio para un futuro dashboard o visualización.

---

## ⚪ FASE 7 (Opcional/Post): Generación de PDF o exportación
⏱ Tiempo espiritual: *“Cuando todo funcione y quieras presumirlo”*

**Objetivos:**
- [ ] Generar versión imprimible de los reportes.
- [ ] Exportar a PDF o CSV.
- [ ] Agregar campos visuales bonitos (plantilla).

---

## 🚫 Fuera de alcance por ahora (y está bien)
- Interfaz gráfica.
- Adjuntar archivos.
- Backup automático.
- Edición de usuarios.

---

## 🧠 Consejo para tu *yo del futuro*
Antes de pensar en PDFs y colores bonitos, asegúrate de que no te truene la lógica cuando un usuario intente hacer un reporte de baja a un equipo inexistente.


## 🗓️ Última actualización
*2025-07-15*
*2025-07-20*


