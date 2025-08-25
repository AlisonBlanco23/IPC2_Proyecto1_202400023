from Nodo import Nodo

class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def agregar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamanio += 1

    def obtener_en(self, indice):
        if indice < 0 or indice >= self._tamanio:
            return None
        actual = self.primero
        for _ in range(indice):
            actual = actual.siguiente
        return actual.contenido

    def buscar_por_atributo(self, atributo, valor):
        actual = self.primero
        indice = 0
        while actual:
            obj = actual.contenido
            if hasattr(obj, atributo) and getattr(obj, atributo) == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1

    def tamanio(self):
        return self._tamanio