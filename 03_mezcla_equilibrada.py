"""
Ejercicio 3: Mezcla Equilibrada (Balanced Merge Sort)
Ordenamiento externo con 2N archivos: N de entrada y N de salida.
Los "archivos" se simulan con listas de corridas (runs).
  1) Se detectan las corridas naturales (tramos ya ordenados) de la secuencia.
  2) Se reparten alternadamente entre los N archivos de entrada.
  3) Se mezclan N corridas (una de cada archivo) en una sola, que se escribe
     en los archivos de salida de forma rotativa.
  4) Los archivos de salida pasan a ser de entrada y se repite hasta que
     queda una sola corrida: la secuencia ordenada.
"""


def corridas_naturales(datos):
    """Divide la secuencia en tramos ascendentes consecutivos."""
    if not datos:
        return []
    corridas = [[datos[0]]]
    for x in datos[1:]:
        if x >= corridas[-1][-1]:
            corridas[-1].append(x)
        else:
            corridas.append([x])
    return corridas


def mezclar_corridas(corridas):
    """Mezcla varias corridas ordenadas en una sola (mezcla de N vías)."""
    posiciones = [0] * len(corridas)
    resultado = []
    while True:
        menor_idx = None
        for k, corrida in enumerate(corridas):
            if posiciones[k] < len(corrida):
                if menor_idx is None or corrida[posiciones[k]] < corridas[menor_idx][posiciones[menor_idx]]:
                    menor_idx = k
        if menor_idx is None:
            break
        resultado.append(corridas[menor_idx][posiciones[menor_idx]])
        posiciones[menor_idx] += 1
    return resultado


def mezcla_equilibrada(datos, n=2, mostrar=True):
    """n = cantidad de archivos de entrada (y de salida)."""
    corridas = corridas_naturales(datos)
    # Distribución inicial en los n archivos de entrada
    entrada = [[] for _ in range(n)]
    for idx, corrida in enumerate(corridas):
        entrada[idx % n].append(corrida)

    pasada = 0
    if mostrar:
        print(f"Corridas iniciales: {len(corridas)}")
        for k, f in enumerate(entrada, 1):
            print(f"  Entrada {k}: {f}")

    while sum(len(f) for f in entrada) > 1:
        pasada += 1
        salida = [[] for _ in range(n)]
        destino = 0
        # Mientras queden corridas en algún archivo de entrada
        while any(entrada):
            grupo = [f.pop(0) for f in entrada if f]   # una corrida por archivo
            salida[destino].append(mezclar_corridas(grupo))
            destino = (destino + 1) % n
        entrada = salida
        if mostrar:
            print(f"\nPasada {pasada}")
            for k, f in enumerate(entrada, 1):
                print(f"  Archivo {k}: {f}")

    return next(f[0] for f in entrada if f)


if __name__ == "__main__":
    print("=== MEZCLA EQUILIBRADA ===")
    opcion = input("¿Usar datos de ejemplo? (s/n): ").strip().lower()
    if opcion == "n":
        datos = [int(x) for x in input("Números separados por espacio: ").split()]
        n = int(input("Número de archivos de entrada (>=2): ") or 2)
    else:
        datos = [31, 7, 50, 12, 18, 3, 45, 60, 22, 9, 14, 80, 2]
        n = 2

    print("Original:", datos)
    resultado = mezcla_equilibrada(datos, n)
    print("\nOrdenado:", resultado)
