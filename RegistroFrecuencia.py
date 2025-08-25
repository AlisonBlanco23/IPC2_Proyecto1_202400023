class RegistroFrecuencia:
    def __init__(self, id_estacion, valor_texto):
        self.id_estacion = id_estacion
        self.valor = int(str(valor_texto).strip())