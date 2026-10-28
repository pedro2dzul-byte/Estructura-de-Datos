
CAPACIDAD_MAXIMA = 50  


def normalizar(texto):
    
    return " ".join(texto.split()).casefold()

# Lista de ingredientes

class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sig = None  # None == NIL


class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def buscar(self, nombre):
        clave = normalizar(nombre)
        actual = self.cabeza
        while actual is not None:
            if normalizar(actual.nombre) == clave:
                return actual
            actual = actual.sig
        return None

    def insertar_final(self, nombre):
        if self.buscar(nombre) is not None:
            return False
        nuevo = NodoIngrediente(" ".join(nombre.split()))
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.sig is not None:
                actual = actual.sig
            actual.sig = nuevo
        return True

    def eliminar(self, nombre):
        clave = normalizar(nombre)
        anterior, actual = None, self.cabeza
        while actual is not None:
            if normalizar(actual.nombre) == clave:
                if anterior is None:          
                    self.cabeza = actual.sig
                else:                          
                    anterior.sig = actual.sig
                return True
            anterior, actual = actual, actual.sig
        return False

    def eliminar_repetidos(self):
        vistos = set()
        anterior, actual = None, self.cabeza
        eliminados = 0
        while actual is not None:
            clave = normalizar(actual.nombre)
            if clave in vistos:
                anterior.sig = actual.sig
                eliminados += 1
            else:
                vistos.add(clave)
                anterior = actual
            actual = actual.sig
        return eliminados

    def a_lista(self):
        resultado, actual = [], self.cabeza
        while actual is not None:
            resultado.append(actual.nombre)
            actual = actual.sig
        return resultado


class Postre:
    def __init__(self, nombre):
        self.nombre = " ".join(nombre.split())
        self.ingredientes = ListaIngredientes()


class Postres:
    def __init__(self, capacidad=CAPACIDAD_MAXIMA):
        self.capacidad = capacidad
        self.arreglo = []  # siempre ordenado alfabéticamente

    
    def _buscar(self, nombre):
        clave = normalizar(nombre)
        bajo, alto = 0, len(self.arreglo) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            actual = normalizar(self.arreglo[medio].nombre)
            if actual == clave:
                return True, medio
            if actual < clave:
                bajo = medio + 1
            else:
                alto = medio - 1
        return False, bajo  # 'bajo' es la posición donde debería insertarse

    
    def imprimir_ingredientes(self, nombre):
        if not self.arreglo:
            return "El arreglo POSTRES está vacío."
        encontrado, pos = self._buscar(nombre)
        if not encontrado:
            return f"El postre '{nombre}' no existe."
        postre = self.arreglo[pos]
        if postre.ingredientes.esta_vacia():
            return f"El postre '{postre.nombre}' no tiene ingredientes (NIL)."
        lineas = [f"Ingredientes de '{postre.nombre}':"]
        lineas += [f"  - {ing}" for ing in postre.ingredientes.a_lista()]
        return "\n".join(lineas)

    
    def insertar_ingredientes(self, nombre, nuevos):
        if not self.arreglo:
            return "El arreglo POSTRES está vacío."
        encontrado, pos = self._buscar(nombre)
        if not encontrado:
            return f"El postre '{nombre}' no existe."
        nuevos = [n for n in nuevos if n.strip()]
        if not nuevos:
            return "No se proporcionó ningún ingrediente."
        lista = self.arreglo[pos].ingredientes
        agregados, repetidos = [], []
        for ing in nuevos:
            (agregados if lista.insertar_final(ing) else repetidos).append(ing)
        msg = []
        if agregados:
            msg.append("Agregados: " + ", ".join(agregados))
        if repetidos:
            msg.append("Ya existían (se omitieron): " + ", ".join(repetidos))
        return "\n".join(msg)

    
    def eliminar_ingrediente(self, nombre, ingrediente):
        if not self.arreglo:
            return "El arreglo POSTRES está vacío."
        encontrado, pos = self._buscar(nombre)
        if not encontrado:
            return f"El postre '{nombre}' no existe."
        lista = self.arreglo[pos].ingredientes
        if lista.esta_vacia():
            return f"El postre '{self.arreglo[pos].nombre}' no tiene ingredientes."
        if not lista.eliminar(ingrediente):
            return f"El ingrediente '{ingrediente}' no está en '{self.arreglo[pos].nombre}'."
        extra = " (el postre quedó sin ingredientes)" if lista.esta_vacia() else ""
        return f"Ingrediente '{ingrediente}' eliminado{extra}."

    
    def alta(self, nombre, ingredientes):
        if not nombre.strip():
            return "El nombre del postre no puede estar vacío."
        if len(self.arreglo) >= self.capacidad:
            return "El arreglo POSTRES está lleno; no se puede dar de alta."
        encontrado, pos = self._buscar(nombre)
        if encontrado:
            return f"El postre '{nombre}' ya existe."
        nuevo = Postre(nombre)
        for ing in ingredientes:
            if ing.strip():
                nuevo.ingredientes.insertar_final(ing)
        self.arreglo.insert(pos, nuevo)  
        return f"Postre '{nuevo.nombre}' dado de alta en la posición {pos}."

    
    def baja(self, nombre):
        if not self.arreglo:
            return "El arreglo POSTRES está vacío."
        encontrado, pos = self._buscar(nombre)
        if not encontrado:
            return f"El postre '{nombre}' no existe."
        eliminado = self.arreglo.pop(pos)  
        eliminado.ingredientes.cabeza = None  
        return f"Postre '{eliminado.nombre}' dado de baja con todos sus ingredientes."

    #  Ejercicio 2: eliminar elementos repetidos 
    def eliminar_repetidos(self):
    
        if not self.arreglo:
            return "El arreglo POSTRES está vacío; no hay nada que depurar."
        postres_elim = ingr_elim = 0
        unicos = []
        for postre in self.arreglo:
            if unicos and normalizar(unicos[-1].nombre) == normalizar(postre.nombre):
                postres_elim += 1  # arreglo ordenado: los repetidos son contiguos
                continue
            ingr_elim += postre.ingredientes.eliminar_repetidos()
            unicos.append(postre)
        self.arreglo = unicos
        return (f"Postres repetidos eliminados: {postres_elim}\n"
                f"Ingredientes repetidos eliminados: {ingr_elim}")

   
    def mostrar(self):
        if not self.arreglo:
            return "POSTRES: (vacío)"
        lineas = ["POSTRES:"]
        for i, p in enumerate(self.arreglo):
            ings = " -> ".join(p.ingredientes.a_lista() + ["NIL"])
            lineas.append(f"  [{i}] {p.nombre}: {ings}")
        return "\n".join(lineas)

# Menú principal

def pedir_lista(mensaje):
    texto = input(mensaje)
    return [x.strip() for x in texto.split(",") if x.strip()]


def main():
    postres = Postres()
    # Datos de ejemplo
    postres.alta("Flan", ["huevo", "leche", "azúcar", "vainilla"])
    postres.alta("Brownie", ["chocolate", "harina", "huevo", "mantequilla"])
    postres.alta("Gelatina", [])

    menu = """
===== MENÚ POSTRES =====
1. Imprimir ingredientes de un postre
2. Insertar ingredientes a un postre
3. Eliminar un ingrediente de un postre
4. Dar de alta un postre
5. Dar de baja un postre
6. Eliminar elementos repetidos
7. Mostrar toda la estructura
0. Salir
Opción: """

    while True:
        opcion = input(menu).strip()
        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            print(postres.imprimir_ingredientes(input("Nombre del postre: ")))
        elif opcion == "2":
            nombre = input("Nombre del postre: ")
            print(postres.insertar_ingredientes(
                nombre, pedir_lista("Nuevos ingredientes (separados por coma): ")))
        elif opcion == "3":
            nombre = input("Nombre del postre: ")
            print(postres.eliminar_ingrediente(nombre, input("Ingrediente a eliminar: ")))
        elif opcion == "4":
            nombre = input("Nombre del nuevo postre: ")
            print(postres.alta(nombre, pedir_lista("Ingredientes (separados por coma): ")))
        elif opcion == "5":
            print(postres.baja(input("Nombre del postre a dar de baja: ")))
        elif opcion == "6":
            print(postres.eliminar_repetidos())
        elif opcion == "7":
            print(postres.mostrar())
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
