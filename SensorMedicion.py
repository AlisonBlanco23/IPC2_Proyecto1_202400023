from ListaEnlazadaSimple import ListaEnlazadaSimple

class SensorMedicion:
    def __init__(self, identificador, denominacion):
        self.id = identificador
        self.nombre = denominacion
        self.registros = ListaEnlazadaSimple()