"""
Ejercicio 3: Búsqueda por Hash
Directorio telefónico implementado con una tabla hash propia.
Las colisiones se resuelven con encadenamiento (listas en cada casilla).
"""


class TablaHash:
    def __init__(self, tamano=10):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def _hash(self, clave):
        """Función hash: suma los códigos de los caracteres y aplica módulo."""
        return sum(ord(c) for c in clave.lower()) % self.tamano

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        for par in self.tabla[indice]:
            if par[0].lower() == clave.lower():   # si ya existe, se actualiza
                par[1] = valor
                return
        self.tabla[indice].append([clave, valor])

    def buscar(self, clave):
        """Devuelve (valor, índice, comparaciones). valor = None si no existe."""
        indice = self._hash(clave)
        comparaciones = 0
        for k, v in self.tabla[indice]:
            comparaciones += 1
            if k.lower() == clave.lower():
                return v, indice, comparaciones
        return None, indice, comparaciones

    def mostrar(self):
        for i, casilla in enumerate(self.tabla):
            contenido = " -> ".join(f"{k}: {v}" for k, v in casilla) or "(vacía)"
            print(f"  [{i}] {contenido}")


def crear_directorio():
    directorio = TablaHash(10)
    contactos = {
        "Ana": "999-123-4567", "Luis": "999-234-5678", "María": "999-345-6789",
        "Carlos": "999-456-7890", "Sofía": "999-567-8901", "Pedro": "999-678-9012",
        "Lucía": "999-789-0123", "Jorge": "999-890-1234",
    }
    for nombre, tel in contactos.items():
        directorio.insertar(nombre, tel)
    return directorio


def ejecutar():
    print("\n=== BÚSQUEDA HASH (Directorio telefónico) ===")
    directorio = crear_directorio()
    while True:
        print("\n  a) Buscar contacto   b) Agregar contacto   c) Ver tabla hash   d) Volver")
        opcion = input("  Elija una opción: ").strip().lower()
        if opcion == "a":
            nombre = input("  Nombre a buscar: ").strip()
            tel, indice, comps = directorio.buscar(nombre)
            if tel:
                print(f"  Teléfono de {nombre}: {tel}")
            else:
                print(f"  '{nombre}' no está en el directorio.")
            print(f"  Casilla consultada: {indice} | Comparaciones: {comps}")
        elif opcion == "b":
            nombre = input("  Nombre: ").strip()
            tel = input("  Teléfono: ").strip()
            if nombre and tel:
                directorio.insertar(nombre, tel)
                print("  Contacto guardado.")
            else:
                print("  Datos incompletos.")
        elif opcion == "c":
            directorio.mostrar()
        elif opcion == "d":
            break
        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    ejecutar()
