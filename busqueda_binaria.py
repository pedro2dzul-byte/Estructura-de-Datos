"""
Ejercicio 2: Búsqueda binaria
Busca una matrícula dentro de una lista de matrículas ORDENADA.
"""

MATRICULAS = [1005, 1012, 1020, 1033, 1047, 1058, 1064, 1079, 1085, 1091,
              1103, 1118, 1126, 1134, 1149, 1152, 1167, 1180, 1195, 1200]


def busqueda_binaria(lista, objetivo, mostrar_pasos=False):
    """Divide la lista a la mitad en cada paso (la lista debe estar ordenada).
    Devuelve (posición, comparaciones). Si no lo encuentra, posición = -1."""
    inicio, fin = 0, len(lista) - 1
    comparaciones = 0
    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        if mostrar_pasos:
            print(f"  Paso {comparaciones}: rango [{inicio}..{fin}], "
                  f"medio = posición {medio} (valor {lista[medio]})")
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            inicio = medio + 1   # buscar en la mitad derecha
        else:
            fin = medio - 1      # buscar en la mitad izquierda
    return -1, comparaciones


def ejecutar():
    print("\n=== BÚSQUEDA BINARIA ===")
    print("Matrículas (ordenadas):", MATRICULAS)
    try:
        objetivo = int(input("¿Qué matrícula desea buscar? "))
    except ValueError:
        print("Debe escribir un número entero.")
        return

    posicion, comparaciones = busqueda_binaria(MATRICULAS, objetivo, mostrar_pasos=True)
    if posicion != -1:
        print(f"Matrícula {objetivo} encontrada en la posición {posicion}.")
    else:
        print(f"La matrícula {objetivo} no existe en la lista.")
    print(f"Comparaciones realizadas: {comparaciones}")


if __name__ == "__main__":
    ejecutar()
