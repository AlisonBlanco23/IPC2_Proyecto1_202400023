class MenuPrincipal:
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
                print("Opción: Cargar archivo")
            elif opcion == "2":
                print("Opción: Procesar archivo")
            elif opcion == "3":
                print("Opción: Escribir archivo salida")
            elif opcion == "4":
                print("Nombre: Alison Melysa Pérez Blanco")
                print("Carné: 202400023")
                print("Curso: Introducción a la Programación y Computación 2")
                print("Carrera: Ingeniería en Ciencias y Sistemas")
                print("Semestre: 4to")
                print("Enlace a documentación: ")
            elif opcion == "5":
                print("Opción: Generar gráfica ")
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrar()
