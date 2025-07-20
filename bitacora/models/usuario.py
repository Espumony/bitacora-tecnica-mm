"""definición de la clase Usuario. Ideal para representar usuarios
 del sistema como objetos (nombre, contraseña, etc.)."""


class Usuario:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"Usuario: {self.username}"

    @classmethod
    def autenticar(cls, conexion,  username, password):
        cursor = conexion.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))

        fila = cursor.fetchone()
        if fila:
            return cls(username)
        else:
            return None  