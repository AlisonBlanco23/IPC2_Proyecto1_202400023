from ListaEnlazadaSimple import ListaEnlazadaSimple
from RegistroFrecuencia import RegistroFrecuencia

class RepresentacionMatriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = ListaEnlazadaSimple()

        for _ in range(filas):
            fila = ListaEnlazadaSimple()
            for _ in range(columnas):
                fila.agregar(RegistroFrecuencia("", "0"))
            self.datos.agregar(fila)

    def asignar(self, fila, col, registro):
        fila_lista = self.datos.obtener_en(fila)
        if fila_lista:
            nodo = fila_lista.primero
            for _ in range(col):
                if nodo:
                    nodo = nodo.siguiente
            if nodo:
                nodo.contenido = registro

    def extraer(self, fila, col):
        fila_lista = self.datos.obtener_en(fila)
        if fila_lista:
            return fila_lista.obtener_en(col)
        return None

    def obtener_patron_fila(self, fila):
        patron = []
        fila_lista = self.datos.obtener_en(fila)
        actual = fila_lista.primero
        while actual:
            valor = 1 if actual.contenido.valor > 0 else 0
            patron.append(valor)
            actual = actual.siguiente
        return tuple(patron)