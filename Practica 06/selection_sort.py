arreglo = [5, 8, 3, 2, 7, 6, 1, 4, 9]

for i in range(len(arreglo)):

    # Suponer que el elemento actual es el menor
    menor = i

    # Buscar el elemento menor en el resto del arreglo
    for j in range(i + 1, len(arreglo)):

        if arreglo[j] < arreglo[menor]:
            menor = j

    # Intercambiar los elementos
    temporal = arreglo[i]
    arreglo[i] = arreglo[menor]
    arreglo[menor] = temporal

print("Arreglo ordenado:", arreglo)