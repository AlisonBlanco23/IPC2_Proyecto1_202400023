from SensorMedicion import SensorMedicion
from ListaEnlazadaSimple import ListaEnlazadaSimple
from CampoAgricola import CampoAgricola
from xml.dom.minidom import parse
import xml.dom.minidom as minidom
from RegistroFrecuencia import RegistroFrecuencia
from EstacionMonitoreo import EstacionMonitoreo

class Sistema_Agricultura:
    def __init__(self):
        self.campos = ListaEnlazadaSimple()
        self.estado_procesado = False

    def cargar_archivo(self, ruta):
        try:
            dom = parse(ruta)
            nodos_campo = dom.getElementsByTagName('campo')

            for nodo in nodos_campo:
                id_campo = nodo.getAttribute('id')
                nombre = nodo.getAttribute('nombre')
                campo = CampoAgricola(id_campo, nombre)
                print(f"Cargando campo: {id_campo}")

                estaciones = nodo.getElementsByTagName('estacion')
                for est in estaciones:
                    id_est = est.getAttribute('id')
                    nombre_est = est.getAttribute('nombre')
                    estacion = EstacionMonitoreo(id_est, nombre_est)
                    campo.estaciones.agregar(estacion)
                    print(f"Estacion registrada: {id_est}")

                sensores_s = nodo.getElementsByTagName('sensorS')
                for sensor in sensores_s:
                    id_s = sensor.getAttribute('id')
                    nombre_s = sensor.getAttribute('nombre')
                    sensor_obj = SensorMedicion(id_s, nombre_s)
                    frecuencias = sensor.getElementsByTagName('frecuencia')
                    for f in frecuencias:
                        id_estacion = f.getAttribute('idEstacion')
                        valor = f.firstChild.nodeValue.strip()
                        frec = RegistroFrecuencia(id_estacion, valor)
                        sensor_obj.registros.agregar(frec)
                    campo.sensores_suelo.agregar(sensor_obj)
                    print(f"Sensor de suelo registrado: {id_s}")

                sensores_t = nodo.getElementsByTagName('sensorT')
                for sensor in sensores_t:
                    id_t = sensor.getAttribute('id')
                    nombre_t = sensor.getAttribute('nombre')
                    sensor_obj = SensorMedicion(id_t, nombre_t)
                    frecuencias = sensor.getElementsByTagName('frecuencia')
                    for f in frecuencias:
                        id_estacion = f.getAttribute('idEstacion')
                        valor = f.firstChild.nodeValue.strip()
                        frec = RegistroFrecuencia(id_estacion, valor)
                        sensor_obj.registros.agregar(frec)
                    campo.sensores_cultivo.agregar(sensor_obj)
                    print(f"Sensor de cultivo registrado: {id_t}")

                campo.construir_matrices_frecuencia()
                campo.construir_matrices_patron()
                self.campos.agregar(campo)

            self.estado_procesado = False
            print("Archivo cargado exitosamente")

        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    def procesar_campos(self):
        if not self.estado_procesado:
            actual = self.campos.primero
            while actual:
                actual.contenido.reducir_estaciones()
                actual = actual.siguiente
            self.estado_procesado = True
            print("Campos procesados correctamente")
        else:
            print("Los campos ya han sido procesados")

    def exportar_resultado(self, ruta_salida):
        if not self.estado_procesado:
            print("Primero debe procesar el archivo")
            return

        doc = minidom.Document()
        raiz = doc.createElement('camposAgricolas')
        doc.appendChild(raiz)

        actual = self.campos.primero
        while actual:
            campo = actual.contenido
            nodo_campo = doc.createElement('campo')
            nodo_campo.setAttribute('id', campo.id)
            nodo_campo.setAttribute('nombre', campo.nombre)

            nodo_est_reducidas = doc.createElement('estacionesBaseReducidas')
            est_actual = campo.estaciones_reducidas.primero
            while est_actual:
                est = est_actual.contenido
                nodo_est = doc.createElement('estacion')
                nodo_est.setAttribute('id', est.id)
                nodo_est.setAttribute('nombre', est.nombre)
                nodo_est_reducidas.appendChild(nodo_est)
                est_actual = est_actual.siguiente
            nodo_campo.appendChild(nodo_est_reducidas)

            nodo_sensores_s = doc.createElement('sensoresSuelo')
            sen_actual = campo.sensores_suelo_reducidos.primero
            while sen_actual:
                sen = sen_actual.contenido
                nodo_sen = doc.createElement('sensorS')
                nodo_sen.setAttribute('id', sen.id)
                nodo_sen.setAttribute('nombre', sen.nombre)
                reg_actual = sen.registros.primero
                while reg_actual:
                    reg = reg_actual.contenido
                    nodo_reg = doc.createElement('frecuencia')
                    nodo_reg.setAttribute('idEstacion', reg.id_estacion)
                    nodo_reg.appendChild(doc.createTextNode(str(reg.valor)))
                    nodo_sen.appendChild(nodo_reg)
                    reg_actual = reg_actual.siguiente
                nodo_sensores_s.appendChild(nodo_sen)
                sen_actual = sen_actual.siguiente
            nodo_campo.appendChild(nodo_sensores_s)

            nodo_sensores_t = doc.createElement('sensoresCultivo')
            sen_actual = campo.sensores_cultivo_reducidos.primero
            while sen_actual:
                sen = sen_actual.contenido
                nodo_sen = doc.createElement('sensorT')
                nodo_sen.setAttribute('id', sen.id)
                nodo_sen.setAttribute('nombre', sen.nombre)
                reg_actual = sen.registros.primero
                while reg_actual:
                    reg = reg_actual.contenido
                    nodo_reg = doc.createElement('frecuencia')
                    nodo_reg.setAttribute('idEstacion', reg.id_estacion)
                    nodo_reg.appendChild(doc.createTextNode(str(reg.valor)))
                    nodo_sen.appendChild(nodo_reg)
                    reg_actual = reg_actual.siguiente
                nodo_sensores_t.appendChild(nodo_sen)
                sen_actual = sen_actual.siguiente
            nodo_campo.appendChild(nodo_sensores_t)

            raiz.appendChild(nodo_campo)
            actual = actual.siguiente

        with open(ruta_salida, 'w', encoding='utf-8') as f:
            doc.writexml(f, indent='', addindent='\t', newl='\n', encoding='utf-8')
        print(f"Archivo de salida guardado: {ruta_salida}")