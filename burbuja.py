
# Ordenamiento por el metodo de Burbuja

numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:", numeros)

for i in range(len(numeros)):
    
    
    for j in range(0, len(numeros) - i - 1):
        
        if numeros[j] > numeros[j + 1]:
            
            auxiliar = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = auxiliar

print("Lista ordenada:", numeros)
