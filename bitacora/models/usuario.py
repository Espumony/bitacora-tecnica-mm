"""definición de la clase Usuario. Ideal para representar usuarios
 del sistema como objetos (nombre, contraseña, etc.)."""


class Usuario:
    def __init__(self, username, nombre, cargo):
        self.username = username
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        return f"{self.username} {self.nombre} {self.cargo} "
    

    @classmethod
    def autenticar(cls, conexion,  username, password):
        cursor = conexion.execute("SELECT username, nombre, cargo FROM usuarios WHERE username = ? AND password = ?", (username, password))

        fila = cursor.fetchone()
        if fila:
            return cls(*fila)
        else:
            return None  