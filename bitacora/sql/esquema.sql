-- Tabla de usuarios autorizados para crear reportes
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    nombre TEXT,
    cargo TEXT
);

-- Tabla de equipos médicos registrados
CREATE TABLE IF NOT EXISTS equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    marca TEXT,
    modelo TEXT,
    id_estado INTEGER,
    FOREIGN KEY (id_estado) REFERENCES estados_equipo(id)

);

-- Tabla con tipos de mantenimiento (instalación, preventivo, correctivo, etc.)
CREATE TABLE IF NOT EXISTS tipos_mantenimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    codigo TEXT
);

-- Tabla principal de reportes realizados
CREATE TABLE IF NOT EXISTS reportes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    folio TEXT,
    fecha TEXT,
    descripcion TEXT,
    id_usuario INTEGER,
    id_equipo INTEGER,
    id_tipo_mantenimiento INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_equipo) REFERENCES equipos(id),
    FOREIGN KEY (id_tipo_mantenimiento) REFERENCES tipos_mantenimiento(id)
);

-- Tabla de estados de los equipos
CREATE TABLE IF NOT EXISTS estados_equipo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

-- Inserta algunos usuarios fijos. Estos serán los únicos válidos.
INSERT OR IGNORE INTO usuarios (username, password)
VALUES
    ('admin', '1234'),
    ('soporte', 'mmsoporte'),
    ('doctorx', 'cura123');

