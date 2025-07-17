

import json

#Clases 

class Equipo:
    def __init__(self, id_equipo, tipo, marca, modelo, estado, fecha):
        self.id_equipo = id_equipo
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo   
        self.estado = estado
        self.fecha = fecha


    def cambiar_estado(self, nuevo_estado):   #Función para cambiar de estado del equipo, solo puede ser llamado por el personal autorizado
        self.estado = nuevo_estado

    def mostrar_informacion(self):
        return f"ID: {self.id_equipo}, Nombre: {self.tipo} {self.marca} {self.modelo}, Estado: {self.estado}, Fecha: {self.fecha}"
    
class Personal:
    def __init__(self, id_personal, nombre, cargo, telefono):
        self.id_personal = id_personal
        self.nombre = nombre
        self.cargo = cargo
        self.telefono = telefono
        self.reportes = []

    def mostrar_informacion(self):
        return f"ID: {self.id_personal}, Nombre: {self.nombre}, Cargo: {self.cargo}, Teléfono: {self.telefono}"
    
    def generar_reporte(self, equipo, tipo_accion, descripcion):
        nuevo_reporte = Reporte(self, equipo, tipo_accion, descripcion)
        self.reportes.append(nuevo_reporte)
        return nuevo_reporte
    
    def consultar_reportes(self):
        return self.reportes
    
class Reporte:
    def __init__(self, personal, equipo, tipo_accion, descripcion):
        self.personal = personal
        self.equipo = equipo
        self.tipo_accion = tipo_accion
        self.descripcion = descripcion

    def informacion_de_reporte(self):
        return f"Reporte por {self.personal.nombre} sobre {self.equipo.tipo} {self.equipo.marca} {self.equipo.modelo}: {self.tipo_accion} - {self.descripcion} - fecha: {self.equipo.fecha}"
    
class Bitacora:
    def __init__(self):
        self.reportes = []
        self.equipos = []
        self.personal = []

    #fUNCIONES PARA AGREGAR EQUIPO Y PERSONAL
    def guardar_en_json(self):
        datos = {
            "reportes": [r.informacion_de_reporte() for r in self.reportes],
            "equipos": [vars(e) for e in self.equipos],
            "personal": [vars(p) for p in self.personal]
        }
        with open('bitacora.json', 'w', encoding= 'utf-8') as archivo:
            json.dump(datos, archivo, indent=4 , ensure_ascii=False)

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
        print(f"Equipo {equipo.tipo} agregado a la bitácora.")
        self.guardar_en_json()

    def agregar_personal(self, personal):
        self.personal.append(personal)
        print(f"Personal {personal.nombre} agregado a la bitácora.")
        self.guardar_en_json()
    
    def agregar_reporte(self, reporte):
        self.reportes.append(reporte)
        print("Reporte agregado.")
        self.guardar_en_json()

    def buscar_por_tecnico(self, nombre):
        return [r for r in self.reportes if r.personal.nombre == nombre]

    def buscar_por_equipo(self, id_equipo):
        return [r for r in self.reportes if r.equipo.id_equipo == id_equipo]
    
    def buscar_por_tipo_accion(self, tipo_accion):
        return [r for r in self.reportes if r.tipo_accion == tipo_accion]
    
    def buscar_por_fecha(self, fecha):
        return [r for r in self.reportes if r.equipo.fecha == fecha]

    def listar_todos(self):
        print("Reportes:")
        for r in self.reportes:
            print("-", r.informacion_de_reporte())

        print("\nEquipos:")
        for e in self.equipos:
            print("-", e.mostrar_informacion())

        print("\nPersonal:")
        for p in self.personal:
            print("-", p.mostrar_informacion())

