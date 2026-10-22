class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def ver_frente(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None

    def __str__(self):
        return str(self.elementos)


def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    
    # Creamos copias temporales o iteramos desencolando (aquí simularemos el recorrido sin destruir las originales si se desea, 
    # o bien usando los elementos internos de forma segura).
    elementos_a = cola_a.elementos
    elementos_b = cola_b.elementos
    
    # Sumar elemento a elemento de manera correspondiente
    for a, b in zip(elementos_a, elementos_b):
        cola_resultado.encolar(a + b)
        
    return cola_resultado

# --- Ejemplo de prueba ---
colaA = Cola()
for num in [3, 4, 2, 8, 12]:
    colaA.encolar(num)

colaB = Cola()
for num in [6, 2, 9, 11, 3]:
    colaB.encolar(num)

cola_res = sumar_colas(colaA, colaB)
print("Cola A:", colaA)
print("Cola B:", colaB)
print("Cola Resultado:", cola_res)