from ListaEnlazadaSimple import ListaEnlazadaSimple
from RepresentacionMatriz import RepresentacionMatriz
from SensorMedicion import SensorMedicion
from EstacionMonitoreo import EstacionMonitoreo
from RegistroFrecuencia import RegistroFrecuencia

class CampoAgricola:
    def __init__(self, identificador, nombre_campo):
        self.id = identificador
        self.nombre = nombre_campo
        self.estaciones = ListaEnlazadaSimple()
        self.sensores_suelo = ListaEnlazadaSimple()
        self.sensores_cultivo = ListaEnlazadaSimple()
        self.matriz_suelo = None
        self.matriz_cultivo = None
        self.matriz_patron_suelo = None
        self.matriz_patron_cultivo = None
        self.estaciones_reducidas = None
        self.sensores_suelo_reducidos = None
        self.sensores_cultivo_reducidos = None

    def construir_matrices_frecuencia(self):
        filas = self.estaciones.tamanio()
        cols_s = self.sensores_suelo.tamanio()
        cols_c = self.sensores_cultivo.tamanio()

        self.matriz_suelo = RepresentacionMatriz(filas, cols_s)
        self.matriz_cultivo = RepresentacionMatriz(filas, cols_c)

        for j in range(cols_s):
            sensor = self.sensores_suelo.obtener_en(j)
            actual = sensor.registros.primero
            while actual:
                reg = actual.contenido
                i = self.estaciones.buscar_por_atributo('id', reg.id_estacion)
                if i != -1:
                    self.matriz_suelo.asignar(i, j, reg)
                actual = actual.siguiente

        for j in range(cols_c):
            sensor = self.sensores_cultivo.obtener_en(j)
            actual = sensor.registros.primero
            while actual:
                reg = actual.contenido
                i = self.estaciones.buscar_por_atributo('id', reg.id_estacion)
                if i != -1:
                    self.matriz_cultivo.asignar(i, j, reg)
                actual = actual.siguiente

    def construir_matrices_patron(self):
        filas = self.estaciones.tamanio()
        cols_s = self.sensores_suelo.tamanio()
        cols_c = self.sensores_cultivo.tamanio()

        self.matriz_patron_suelo = RepresentacionMatriz(filas, cols_s)
        self.matriz_patron_cultivo = RepresentacionMatriz(filas, cols_c)

        for i in range(filas):
            for j in range(cols_s):
                reg = self.matriz_suelo.extraer(i, j)
                valor = 1 if reg.valor > 0 else 0
                self.matriz_patron_suelo.asignar(i, j, RegistroFrecuencia("", str(valor)))

            for j in range(cols_c):
                reg = self.matriz_cultivo.extraer(i, j)
                valor = 1 if reg.valor > 0 else 0
                self.matriz_patron_cultivo.asignar(i, j, RegistroFrecuencia("", str(valor)))

    def reducir_estaciones(self):
        grupos = {}
        for i in range(self.estaciones.tamanio()):
            pat_s = self.matriz_patron_suelo.obtener_patron_fila(i)
            pat_c = self.matriz_patron_cultivo.obtener_patron_fila(i)
            clave = (pat_s, pat_c)
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(i)

        self.estaciones_reducidas = ListaEnlazadaSimple()
        self.sensores_suelo_reducidos = ListaEnlazadaSimple()
        self.sensores_cultivo_reducidos = ListaEnlazadaSimple()

        id_reducido = 1
        for indices in grupos.values():
            nombres = [self.estaciones.obtener_en(i).nombre for i in indices]
            nueva_estacion = EstacionMonitoreo(f"r{id_reducido}", ", ".join(nombres))
            self.estaciones_reducidas.agregar(nueva_estacion)

            for j in range(self.sensores_suelo.tamanio()):
                sensor_original = self.sensores_suelo.obtener_en(j)
                if self.sensores_suelo_reducidos.obtener_en(j) is None:
                    nuevo_sensor = SensorMedicion(sensor_original.id, sensor_original.nombre)
                    self.sensores_suelo_reducidos.agregar(nuevo_sensor)
                suma = sum(self.matriz_suelo.extraer(i, j).valor for i in indices)
                if suma > 0:
                    frec_nueva = RegistroFrecuencia(f"r{id_reducido}", str(suma))
                    self.sensores_suelo_reducidos.obtener_en(j).registros.agregar(frec_nueva)

            for j in range(self.sensores_cultivo.tamanio()):
                sensor_original = self.sensores_cultivo.obtener_en(j)
                if self.sensores_cultivo_reducidos.obtener_en(j) is None:
                    nuevo_sensor = SensorMedicion(sensor_original.id, sensor_original.nombre)
                    self.sensores_cultivo_reducidos.agregar(nuevo_sensor)
                suma = sum(self.matriz_cultivo.extraer(i, j).valor for i in indices)
                if suma > 0:
                    frec_nueva = RegistroFrecuencia(f"r{id_reducido}", str(suma))
                    self.sensores_cultivo_reducidos.obtener_en(j).registros.agregar(frec_nueva)

            id_reducido += 1