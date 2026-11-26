"""
Programa principal: menú para ejecutar los 3 métodos de búsqueda.
Archivos necesarios en la misma carpeta:
    busqueda_secuencial.py, busqueda_binaria.py, busqueda_hash.py
"""

import busqueda_secuencial
import busqueda_binaria
import busqueda_hash


def mostrar_menu():
    print("\n==============================")
    print("   MÉTODOS DE BÚSQUEDA")
    print("==============================")
    print("1. Búsqueda secuencial")
    print("2. Búsqueda binaria")
    print("3. Búsqueda hash")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            busqueda_secuencial.ejecutar()
        elif opcion == "2":
            busqueda_binaria.ejecutar()
        elif opcion == "3":
            busqueda_hash.ejecutar()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
