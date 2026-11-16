
# Ordenamiento por el metodo de Seleccion

numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:", numeros)


for i in range(len(numeros)):

    menor = i

   
    for j in range(i + 1, len(numeros)):

        if numeros[j] < numeros[menor]:
            menor = j

    
    auxiliar = numeros[i]
    numeros[i] = numeros[menor]
    numeros[menor] = auxiliar

print("Lista ordenada:", numeros)
