--script SQL donde defines cómo se ven tus tablas (usuarios, clientes, etc.).

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- Inserta algunos usuarios fijos. Estos serán los únicos válidos.
INSERT OR IGNORE INTO usuarios (username, password)
VALUES
    ('admin', '1234'),
    ('soporte', 'mmsoporte'),
    ('doctorx', 'cura123');
