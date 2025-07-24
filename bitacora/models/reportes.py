"""Constructor de los reportes, aquí van a estar los metodos para generar reportes
el método generar reporte tiene que estar ligado a una sesión actual de usuario
La cual insertará el nombre del usuario, también al interactuar con un equipo
pasa a cambiar el estado de un equipo guardado en la db, cuando se seleccione 
tipo de servicio instalación se agrega una entrada nueva a la bd de equipos esto 
generará un nuevo equipo en la base de datos"""

class Reporte:
    def __init__(self, id_usuario, id_equipo, descripcion, id_tipo_reporte):
        self.id_usuario = id_usuario
        self.id_equipo = id_equipo
        self.descripcion = descripcion
        self.id_tipo_reporte = id_tipo_reporte

    @classmethod

    def solicitar_datos_y_generar_reporte(cls, usuario):
        pass
    
    def generar_reporte(cls, conexion, username, equipo_id, descripcion, tipo_reporte_id):

        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO reportes (username, descripcion)
            VALUES (?, ?)
        """, (username, descripcion))
        conexion.commit()
        print("📝 Reporte guardado exitosamente.")

    def mostrar_reporte(self):
        # Aquí se implementaría la lógica para mostrar el reporte generado
        pass


