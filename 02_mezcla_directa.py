"""
Ejercicio 2: Mezcla Directa (Straight Merge Sort)
Ordenamiento externo. Los "archivos" se simulan con listas.
En cada pasada:
  1) DISTRIBUCIÓN: la secuencia se reparte en dos auxiliares (B y C),
     alternando bloques de tamaño 'longitud'.
  2) MEZCLA: se combinan bloques de B y C (ya ordenados) en la secuencia A.
La longitud del bloque se duplica en cada pasada: 1, 2, 4, 8, ...
"""


def distribuir(a, longitud):
    """Reparte A en B y C alternando bloques de 'longitud' elementos."""
    b, c = [], []
    destino = b
    for inicio in range(0, len(a), longitud):
        destino.extend(a[inicio:inicio + longitud])
        destino = c if destino is b else b
    return b, c


def mezclar(b, c, longitud):
    """Mezcla bloques de 'longitud' de B y C, produciendo bloques de 2*longitud."""
    a = []
    i = j = 0
    while i < len(b) or j < len(c):
        fin_i = min(i + longitud, len(b))
        fin_j = min(j + longitud, len(c))
        # Mezclar un bloque de B con un bloque de C
        while i < fin_i and j < fin_j:
            if b[i] <= c[j]:
                a.append(b[i])
                i += 1
            else:
                a.append(c[j])
                j += 1
        a.extend(b[i:fin_i])
        a.extend(c[j:fin_j])
        i, j = fin_i, fin_j
    return a


def mezcla_directa(datos, mostrar=True):
    a = list(datos)
    longitud = 1
    pasada = 0
    while longitud < len(a):
        pasada += 1
        b, c = distribuir(a, longitud)
        a = mezclar(b, c, longitud)
        if mostrar:
            print(f"\nPasada {pasada} (bloques de {longitud})")
            print("  B:", b)
            print("  C:", c)
            print("  A:", a)
        longitud *= 2
    return a


if __name__ == "__main__":
    print("=== MEZCLA DIRECTA ===")
    opcion = input("¿Usar datos de ejemplo? (s/n): ").strip().lower()
    if opcion == "n":
        datos = [int(x) for x in input("Números separados por espacio: ").split()]
    else:
        datos = [44, 55, 12, 42, 94, 18, 6, 67]

    print("Original:", datos)
    resultado = mezcla_directa(datos)
    print("\nOrdenado:", resultado)
