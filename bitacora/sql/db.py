"""funciones para conectar a la base de datos, crear tablas, etc."""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "database", "mm.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    with conectar() as con:
        with open(os.path.join(os.path.dirname(__file__), "esquema.sql"), "r", encoding="utf-8") as f:
            con.executescript(f.read())
