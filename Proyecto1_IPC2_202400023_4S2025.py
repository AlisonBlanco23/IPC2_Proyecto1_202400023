import xml.etree.ElementTree as ET

class MenuPrincipal:
    def __init__(self):
        self.gestor = GestorDatos()

    def mostrar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Cargar archivo")
            print("2. Procesar archivo")
            print("3. Escribir archivo salida")
            print("4. Mostrar datos del estudiante")
            print("5. Generar gráfica")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestor.cargar_archivo()
            elif opcion == "2":
                print("Opción: Procesar archivo (Release 3)")
            elif opcion == "3":
                print("Opción: Escribir archivo salida (Release 3)")
            elif opcion == "4":
                print("Nombre: Alison Melysa Pérez Blanco")
                print("Carné: 202400023")
                print("Curso: Introducción a la Programación y Computación 2")
                print("Carrera: Ingeniería en Ciencias y Sistemas")
                print("Semestre: 4to")
                print("Enlace a documentación: ")
            elif opcion == "5":
                print("Opción: Generar gráfica (Release 4)")
            elif opcion == "6":
                print("Gracias por tu visita.")
                break
            else:
                print("Opción no válida, intente de nuevo.")

class GestorDatos:
    def __init__(self):
        self.campos = Lista()

    def cargar_archivo(self):
        ruta = input("Ingrese la ruta del archivo XML: ")
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            for campo in root.findall("campo"):
                id_campo = campo.get("id")
                nombre_campo = campo.get("nombre")
                print(f"Cargando {nombre_campo}")
                nuevo_campo = Campo(id_campo, nombre_campo)

                estaciones = campo.find("estacionesBase")
                if estaciones is not None:
                    for estacion in estaciones.findall("estacion"):
                        est = Estacion(estacion.get("id"), estacion.get("nombre"))
                        print(f"Creando estación base {est.id}")
                        nuevo_campo.estaciones.agregar(est)

                sensores_suelo = campo.find("sensoresSuelo")
                if sensores_suelo is not None:
                    for sensor in sensores_suelo.findall("sensorS"):
                        s = SensorSuelo(sensor.get("id"), sensor.get("nombre"))
                        print(f"Creando sensor de suelo {s.id}")
                        nuevo_campo.sensores_suelo.agregar(s)

                sensores_cultivo = campo.find("sensoresCultivo")
                if sensores_cultivo is not None:
                    for sensor in sensores_cultivo.findall("sensorT"):
                        t = SensorCultivo(sensor.get("id"), sensor.get("nombre"))
                        print(f"Creando sensor de cultivo {t.id}")
                        nuevo_campo.sensores_cultivo.agregar(t)

                self.campos.agregar(nuevo_campo)

            print("Archivo cargado correctamente.")

        except Exception as e:
            print("Error al cargar archivo:", e)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.primero = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

class Estacion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Estación {self.id} - {self.nombre}"

class SensorSuelo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.frecuencias = Lista()

    def __str__(self):
        return f"Sensor de Suelo {self.id} - {self.nombre}"

class SensorCultivo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.frecuencias = Lista()

    def __str__(self):
        return f"Sensor de Cultivo {self.id} - {self.nombre}"

class Campo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.estaciones = Lista()
        self.sensores_suelo = Lista()
        self.sensores_cultivo = Lista()

    def __str__(self):
        return f"Campo {self.id} - {self.nombre}"

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrar()
