"""
Ejercicio 1: Intercalación
Combina dos listas YA ORDENADAS en una sola lista ordenada,
comparando el primer elemento pendiente de cada una.
"""


def intercalar(a, b):
    """Intercala dos listas ordenadas ascendentemente en una nueva lista ordenada."""
    resultado = []
    i = j = 0

    # Mientras ambas listas tengan elementos, se pasa el menor al resultado
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    # Una de las dos se agotó: se copia lo que sobra de la otra
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


def leer_lista(mensaje):
    """Lee números separados por espacios y los devuelve ordenados."""
    texto = input(mensaje)
    return sorted(int(x) for x in texto.split())


if __name__ == "__main__":
    print("=== INTERCALACIÓN DE DOS LISTAS ORDENADAS ===")
    opcion = input("¿Usar datos de ejemplo? (s/n): ").strip().lower()

    if opcion == "n":
        lista_a = leer_lista("Lista A (números separados por espacio): ")
        lista_b = leer_lista("Lista B (números separados por espacio): ")
    else:
        lista_a = [3, 8, 15, 20, 42]
        lista_b = [1, 5, 9, 16, 30, 50, 61]

    print("\nLista A:", lista_a)
    print("Lista B:", lista_b)
    print("Intercalada:", intercalar(lista_a, lista_b))
