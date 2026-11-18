
# ---------------------------------------------------------------------------
# 1. ShellSort
# ---------------------------------------------------------------------------
def shell_sort(datos):
    
    a = list(datos)
    n = len(a)
    salto = n // 2
    while salto > 0:
        for i in range(salto, n):
            temp = a[i]
            j = i
            while j >= salto and a[j - salto] > temp:
                a[j] = a[j - salto]
                j -= salto
            a[j] = temp
        salto //= 2
    return a


# ---------------------------------------------------------------------------
# 2. QuickSort 
# ---------------------------------------------------------------------------
def _particion(a, bajo, alto):
    
    medio = (bajo + alto) // 2
    if a[medio] < a[bajo]:
        a[medio], a[bajo] = a[bajo], a[medio]
    if a[alto] < a[bajo]:
        a[alto], a[bajo] = a[bajo], a[alto]
    if a[alto] < a[medio]:
        a[alto], a[medio] = a[medio], a[alto]
    
    a[medio], a[alto] = a[alto], a[medio]
    pivote = a[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if a[j] <= pivote:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[alto] = a[alto], a[i + 1]
    return i + 1


def quick_sort(datos):
    
    a = list(datos)
    if len(a) < 2:
        return a
    pila = [(0, len(a) - 1)]
    while pila:
        bajo, alto = pila.pop()
        if bajo < alto:
            p = _particion(a, bajo, alto)
            pila.append((bajo, p - 1))
            pila.append((p + 1, alto))
    return a


# ---------------------------------------------------------------------------
# 3. HeapSort
# ---------------------------------------------------------------------------
def _heapify(a, n, i):
    
    while True:
        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2
        if izq < n and a[izq] > a[mayor]:
            mayor = izq
        if der < n and a[der] > a[mayor]:
            mayor = der
        if mayor == i:
            return
        a[i], a[mayor] = a[mayor], a[i]
        i = mayor


def heap_sort(datos):
    
    a = list(datos)
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):   
        _heapify(a, n, i)
    for fin in range(n - 1, 0, -1):       
        a[0], a[fin] = a[fin], a[0]
        _heapify(a, fin, 0)
    return a


# ---------------------------------------------------------------------------
# 4. Radix Sort 
# ---------------------------------------------------------------------------
def _counting_por_digito(a, exp):
    n = len(a)
    salida = [0] * n
    conteo = [0] * 10
    for x in a:
        conteo[(x // exp) % 10] += 1
    for d in range(1, 10):
        conteo[d] += conteo[d - 1]
    for i in range(n - 1, -1, -1):        
        d = (a[i] // exp) % 10
        conteo[d] -= 1
        salida[conteo[d]] = a[i]
    return salida


def _radix_positivos(a):
    if not a:
        return a
    maximo = max(a)
    exp = 1
    while maximo // exp > 0:
        a = _counting_por_digito(a, exp)
        exp *= 10
    return a


def radix_sort(datos):
    
    negativos = [-x for x in datos if x < 0]
    positivos = [x for x in datos if x >= 0]
    neg_ordenados = [-x for x in reversed(_radix_positivos(negativos))]
    return neg_ordenados + _radix_positivos(positivos)


# ---------------------------------------------------------------------------
# Menú
# ---------------------------------------------------------------------------
METODOS = {
    "1": ("ShellSort", shell_sort),
    "2": ("QuickSort", quick_sort),
    "3": ("HeapSort", heap_sort),
    "4": ("Radix Sort", radix_sort),
}


def mostrar_menu():
    print("\n===== MÉTODOS DE ORDENAMIENTO =====")
    print("1. ShellSort")
    print("2. QuickSort")
    print("3. HeapSort")
    print("4. Radix Sort")
    print("5. Salir")


def pedir_cantidad():
    while True:
        try:
            n = int(input("¿Cuántos números desea ordenar? "))
            if n > 0:
                return n
            print("Ingrese una cantidad mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


def pedir_numeros(n):
    """Pide n números enteros (separados por espacio o coma, en una o varias líneas)."""
    print(f"Ingrese los {n} números enteros (separados por espacios o comas):")
    numeros = []
    while len(numeros) < n:
        linea = input("> ").replace(",", " ").split()
        try:
            nuevos = [int(x) for x in linea]
        except ValueError:
            print("Hay valores que no son enteros. Intente de nuevo esa línea.")
            continue
        numeros.extend(nuevos)
        if len(numeros) > n:
            print(f"Ingresó más de {n} números; se usarán solo los primeros {n}.")
            numeros = numeros[:n]
    return numeros


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break
        if opcion not in METODOS:
            print("Opción inválida. Elija un número del 1 al 5.")
            continue

        nombre, funcion = METODOS[opcion]
        n = pedir_cantidad()
        numeros = pedir_numeros(n)

        print(f"\nNúmeros originales : {numeros}")
        print(f"Ordenados con {nombre}: {funcion(numeros)}")


if __name__ == "__main__":
    main()
