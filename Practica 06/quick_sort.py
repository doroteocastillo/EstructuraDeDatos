arreglo = [5, 8, 3, 2, 7, 6]

def quicksort(arreglo):

    # Caso base: si tiene 1 o 0 elementos, ya está ordenado
    if len(arreglo) <= 1:
        return arreglo

    # Seleccionar el pivote
    average = (arreglo[0] + arreglo[len(arreglo)-1] + arreglo[len(arreglo)//2]) // 3
    pivote = arreglo[average]

    # Crear dos arreglos
    menores = []
    mayores = []

    # Clasificar los elementos
    for i in range(1, len(arreglo)):

        if arreglo[i] < pivote:
            menores.append(arreglo[i])
        else:
            mayores.append(arreglo[i])

    # Ordenar recursivamente y unir los resultados
    return quicksort(menores) + [pivote] + quicksort(mayores)


resultado = quicksort(arreglo)

print("Arreglo ordenado:", resultado)