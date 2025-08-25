from Sistema_Agricultura import Sistema_Agricultura
from GeneradorGraficas import generar_grafica
import os

def mostrar_menu():
    print("\n" + "="*50)
    print("     SISTEMA DE AGRICULTURA DE PRECISION")
    print("="*50)
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Exportar Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Gráfica")
    print("6. Salir")
    print("="*50)

def main():
    sistema = Sistema_Agricultura()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print("\nCargar Archivo")
            ruta = input("Ruta de la carpeta (opcional): ").strip()
            nombre = input("Nombre del archivo: ").strip()
            archivo = os.path.join(ruta, nombre) if ruta else nombre
            sistema.cargar_archivo(archivo)

        elif opcion == "2":
            print("\nProcesar Archivo")
            sistema.procesar_campos()

        elif opcion == "3":
            print("\nExportar Resultado")
            ruta_salida = input("Ruta de salida (opcional): ").strip()
            nombre_salida = input("Nombre del archivo de salida: ").strip()
            archivo_salida = os.path.join(ruta_salida, nombre_salida) if ruta_salida else nombre_salida
            sistema.exportar_resultado(archivo_salida)

        elif opcion == "4":
            print("\nDatos del Estudiante")
            print("Nombre: Alison Melysa Pérez Blanco")
            print("Carnet: 202400023")
            print("Curso: Introducción a la Programación y Computación 2")
            print("Carrera: Ingenieria en Ciencias y Sistemas")
            print("Semestre: 4to")
            print("Enlace: https://github.com/AlisonBlanco23/IPC2_Proyecto1_202400023")

        elif opcion == "5":
            print("\nGenerar Grafica")
            if sistema.campos.primero is None:
                print("Primero debe cargar un archivo.")
                continue

            actual = sistema.campos.primero
            print("Campos disponibles:")
            while actual:
                campo = actual.contenido
                print(f" - {campo.id}: {campo.nombre}")
                actual = actual.siguiente

            id_campo = input("ID del campo: ").strip()
            tipo = input("Tipo (frecuencia, patron, reducida): ").strip().lower()
            nombre_salida = input("Nombre base para la grafica: ").strip()

            actual = sistema.campos.primero
            encontrado = False
            while actual:
                campo = actual.contenido
                if campo.id == id_campo:
                    if tipo == "frecuencia":
                        generar_grafica(campo.matriz_suelo, f"Matriz Frecuencia Suelo - {id_campo}", campo.estaciones, campo.sensores_suelo, nombre_salida + "_frec_suelo")
                        generar_grafica(campo.matriz_cultivo, f"Matriz Frecuencia Cultivo - {id_campo}", campo.estaciones, campo.sensores_cultivo, nombre_salida + "_frec_cultivo")
                    elif tipo == "patron":
                        if sistema.estado_procesado:
                            generar_grafica(campo.matriz_patron_suelo, f"Matriz Patron Suelo - {id_campo}", campo.estaciones, campo.sensores_suelo, nombre_salida + "_patron_suelo")
                            generar_grafica(campo.matriz_patron_cultivo, f"Matriz Patron Cultivo - {id_campo}", campo.estaciones, campo.sensores_cultivo, nombre_salida + "_patron_cultivo")
                        else:
                            print("Primero procese el archivo.")
                    elif tipo == "reducida":
                        if sistema.estado_procesado:
                            generar_grafica(campo.sensores_suelo_reducidos, f"Matriz Reducida Suelo - {id_campo}", campo.estaciones_reducidas, campo.sensores_suelo_reducidos, nombre_salida + "_reducida_suelo")
                            generar_grafica(campo.sensores_cultivo_reducidos, f"Matriz Reducida Cultivo - {id_campo}", campo.estaciones_reducidas, campo.sensores_cultivo_reducidos, nombre_salida + "_reducida_cultivo")
                        else:
                            print("Primero procese el archivo.")
                    else:
                        print("Tipo no valido.")
                    encontrado = True
                    break
                actual = actual.siguiente

            if not encontrado:
                print("Campo no encontrado.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()