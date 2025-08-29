# Principal.py
from Sistema_Agricultura import Sistema_Agricultura
from GeneradorGraficas import generar_grafica
import os

def mostrar_menu():
    print("\n" + "="*60)
    print("     SISTEMA DE AGRICULTURA DE PRECISION")
    print("="*60)
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Gráfica")
    print("6. Salir")
    print("="*60)

def main():
    sistema = Sistema_Agricultura()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print("\n" + "="*60)
            print("Cargar Archivo")
            print("="*60)
            ruta = input("Ingrese la ruta del archivo: ").strip()
            nombre = input("Ingrese el nombre del archivo: ").strip()
            archivo = os.path.join(ruta, nombre) if ruta else nombre
            sistema.cargar_archivo(archivo)

        elif opcion == "2":
            print("\n" + "="*60)
            print("Procesar Archivo")
            print("="*60)
            sistema.procesar_campos()

        elif opcion == "3":
            print("\n" + "="*60)
            print("Exportar Resultado")
            print("="*60)
            ruta_salida = input("Ingrese la ruta del archivo de salida: ").strip()
            nombre_salida = input("Ingrese el nombre del archivo de salida: ").strip()
            archivo_salida = os.path.join(ruta_salida, nombre_salida) if ruta_salida else nombre_salida
            sistema.exportar_resultado(archivo_salida)

        elif opcion == "4":
            print("\n" + "="*60)
            print("Datos del Estudiante")
            print("="*60)
            print("Nombre: Alison Melysa Pérez Blanco")
            print("Carnet: 202400023")
            print("Curso: Introducción a la Programación y Computación 2")
            print("Carrera: Ingenieria en Ciencias y Sistemas")
            print("Semestre: 4to")
            print("Enlace: https://github.com/AlisonBlanco23/IPC2_Proyecto1_202400023")
            print("="*60)

        elif opcion == "5":
            print("\n" + "="*60)
            print("Generar Grafica")
            print("="*60)

            if not sistema.archivo_cargado:
                print("Primero debe cargar un archivo.")
                print("="*60)
                continue

            if not sistema.procesado:
                print("Primero debe procesar el archivo.")
                print("="*60)
                continue

            actual = sistema.campos.primero
            print("Campos disponibles:")
            while actual:
                campo = actual.contenido
                print(f" - {campo.id}: {campo.nombre}")
                actual = actual.siguiente

            print("\n" + "="*60)
            id_campo = input("ID del campo: ").strip()
            print("\n" + "="*60)
            print("Tipo de matriz:")
            print("1. Frecuencia")
            print("2. Patron")
            print("3. Reducida")
            print("="*60)
            tipo_op = input("Seleccione una opcion (1-3): ").strip()

            nombre_salida = input("Nombre base para la grafica: ").strip()
            print("\n" + "="*60)

            actual = sistema.campos.primero
            encontrado = False
            while actual:
                campo = actual.contenido
                if campo.id == id_campo:
                    if tipo_op == "1":
                        print("\n--- Matriz de Frecuencia (Suelo) ---")
                        campo.mostrar_matriz(campo.matriz_suelo, "Matriz Frecuencia Suelo", campo.estaciones, campo.sensores_suelo)
                        generar_grafica(campo.matriz_suelo, f"Frecuencia Suelo - Campo {id_campo}", campo.estaciones, campo.sensores_suelo, f"{nombre_salida}_frec_suelo")
                        
                        print("\n" + "="*60)
                        print("\n--- Matriz de Frecuencia (Cultivo) ---")
                        campo.mostrar_matriz(campo.matriz_cultivo, "Matriz Frecuencia Cultivo", campo.estaciones, campo.sensores_cultivo)
                        generar_grafica(campo.matriz_cultivo, f"Frecuencia Cultivo - Campo {id_campo}", campo.estaciones, campo.sensores_cultivo, f"{nombre_salida}_frec_cultivo")

                    elif tipo_op == "2":
                        print("\n--- Matriz de Patron (Suelo) ---")
                        campo.mostrar_matriz(campo.matriz_patron_suelo, "Matriz Patron Suelo", campo.estaciones, campo.sensores_suelo)
                        generar_grafica(campo.matriz_patron_suelo, f"Patron Suelo - Campo {id_campo}", campo.estaciones, campo.sensores_suelo, f"{nombre_salida}_patron_suelo")

                        print("\n" + "="*60)
                        print("\n--- Matriz de Patron (Cultivo) ---")
                        campo.mostrar_matriz(campo.matriz_patron_cultivo, "Matriz Patron Cultivo", campo.estaciones, campo.sensores_cultivo)
                        generar_grafica(campo.matriz_patron_cultivo, f"Patron Cultivo - Campo {id_campo}", campo.estaciones, campo.sensores_cultivo, f"{nombre_salida}_patron_cultivo")

                    elif tipo_op == "3":
                        matriz_reducida_s = campo.obtener_matriz_reducida_suelo()
                        matriz_reducida_c = campo.obtener_matriz_reducida_cultivo()

                        print("\n--- Matriz Reducida (Suelo) ---")
                        campo.mostrar_matriz(matriz_reducida_s, "Matriz Reducida Suelo", campo.estaciones_reducidas, campo.sensores_suelo_reducidos)
                        generar_grafica(matriz_reducida_s, f"Reducida Suelo - Campo {id_campo}", campo.estaciones_reducidas, campo.sensores_suelo_reducidos, f"{nombre_salida}_reducida_suelo")

                        print("\n" + "="*60)
                        print("\n--- Matriz Reducida (Cultivo) ---")
                        campo.mostrar_matriz(matriz_reducida_c, "Matriz Reducida Cultivo", campo.estaciones_reducidas, campo.sensores_cultivo_reducidos)
                        generar_grafica(matriz_reducida_c, f"Reducida Cultivo - Campo {id_campo}", campo.estaciones_reducidas, campo.sensores_cultivo_reducidos, f"{nombre_salida}_reducida_cultivo")

                    else:
                        print("Opcion no valida.")
                    encontrado = True
                    break
                actual = actual.siguiente

            if not encontrado:
                print("Campo no encontrado.")
            print("="*60)

        elif opcion == "6":
            print("\n" + "="*60)
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpcion no valida.")
            print("="*60)

if __name__ == "__main__":
    main()