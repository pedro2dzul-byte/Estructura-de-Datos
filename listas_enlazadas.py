class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

def agregar_inicio(inicio, info):
    nuevo = Nodo(info)
    nuevo.liga = inicio
    return nuevo

def agregar_final(inicio, info):
    nuevo = Nodo(info)
    if inicio is None:
        return nuevo
    actual = inicio
    while actual.liga is not None:
        actual = actual.liga
    actual.liga = nuevo
    return inicio

def recorrer_lista(inicio):
    actual = inicio
    if actual is None:
        print("La lista está vacía.")
        return
    while actual is not None:
        print(actual.info, end=" -> ")
        actual = actual.liga
    print("NIL")

def quitar_nodo(inicio, info):
    if inicio is None:
        print("La lista está vacía.")
        return None

    if inicio.info == info:
        return inicio.liga

    anterior = inicio
    actual = inicio.liga

    while actual is not None:
        if actual.info == info:
            anterior.liga = actual.liga
            print(f"Nodo '{info}' eliminado exitosamente.")
            return inicio
        anterior = actual
        actual = actual.liga

    print("No se encontró el nodo:", info)
    return inicio

def crear_por_inicio_interactivo():
    inicio = None
    print("\n--- CREAR LISTA AGREGANDO AL INICIO ---")
    
    # Primer nodo obligatorio
    info = input("Ingrese la información del primer nodo: ")
    inicio = Nodo(info)
    
    res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: ")
    while res == "1":
        info = input("Ingrese la información del nuevo nodo: ")
        inicio = agregar_inicio(inicio, info)
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: ")
        
    return inicio

def crear_por_final_interactivo():
    inicio = None
    print("\n--- CREAR LISTA AGREGANDO AL FINAL ---")
    
    res = "1"
    primero = True
    while res == "1":
        info = input("Ingrese la información del nodo: ")
        if primero:
            inicio = Nodo(info)
            primero = False
        else:
            inicio = agregar_final(inicio, info)
            
        res = input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: ")
        
    return inicio

def menu_principal():
    mi_lista = None
    
    while True:
        print("\n========================================")
        print("       MENÚ DE LISTAS ENLAZADAS         ")
        print("========================================")
        print("1. Crear lista (Agregando al INICIO - Estilo Algoritmo 5.1)")
        print("2. Crear lista (Agregando al FINAL)")
        print("3. Recorrer y mostrar lista")
        print("4. Agregar un nodo individual al inicio")
        print("5. Agregar un nodo individual al final")
        print("6. Quitar un nodo específico")
        print("7. Ejecutar demostración de nodos compartidos (A y B -> C)")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mi_lista = crear_por_inicio_interactivo()
            print("\nLista creada con éxito:")
            recorrer_lista(mi_lista)
            
        elif opcion == "2":
            mi_lista = crear_por_final_interactivo()
            print("\nLista creada con éxito:")
            recorrer_lista(mi_lista)
            
        elif opcion == "3":
            print("\nEstado actual de la lista:")
            recorrer_lista(mi_lista)
            
        elif opcion == "4":
            valor = input("Ingrese el valor del nodo a agregar al inicio: ")
            mi_lista = agregar_inicio(mi_lista, valor)
            print(f"Nodo '{valor}' agregado.")
            recorrer_lista(mi_lista)
            
        elif opcion == "5":
            valor = input("Ingrese el valor del nodo a agregar al final: ")
            mi_lista = agregar_final(mi_lista, valor)
            print(f"Nodo '{valor}' agregado.")
            recorrer_lista(mi_lista)
            
        elif opcion == "6":
            valor = input("Ingrese el valor del nodo que desea eliminar: ")
            mi_lista = quitar_nodo(mi_lista, valor)
            recorrer_lista(mi_lista)
            
        elif opcion == "7":
            print("\n=== DEMOSTRACIÓN: Nodos A y B apuntando al mismo nodo C ===")
            A = Nodo("A")
            B = Nodo("B")
            C = Nodo("C")
            A.liga = C
            B.liga = C
            
            print("Lista desde A:", end=" ")
            recorrer_lista(A)
            print("Lista desde B:", end=" ")
            recorrer_lista(B)
            
            if A.liga is B.liga:
                print("-> ¡Comprobado! A y B apuntan exactamente al mismo nodo en memoria (C).")
                
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()