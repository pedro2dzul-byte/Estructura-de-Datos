"""
Ejercicio 1: Búsqueda secuencial (lineal)
Busca un producto dentro de un inventario NO ordenado.
"""

INVENTARIO = [
    "Lápiz", "Cuaderno", "Borrador", "Regla", "Tijeras",
    "Pegamento", "Marcador", "Calculadora", "Mochila", "Folder",
]


def busqueda_secuencial(lista, objetivo):
    """Recorre la lista elemento por elemento.
    Devuelve (posición, comparaciones). Si no lo encuentra, posición = -1."""
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento.lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones


def ejecutar():
    print("\n=== BÚSQUEDA SECUENCIAL ===")
    print("Inventario:", ", ".join(INVENTARIO))
    objetivo = input("¿Qué producto desea buscar? ").strip()
    if not objetivo:
        print("No escribió ningún producto.")
        return

    posicion, comparaciones = busqueda_secuencial(INVENTARIO, objetivo)
    if posicion != -1:
        print(f"'{INVENTARIO[posicion]}' encontrado en la posición {posicion}.")
    else:
        print(f"'{objetivo}' no está en el inventario.")
    print(f"Comparaciones realizadas: {comparaciones}")


if __name__ == "__main__":
    ejecutar()
