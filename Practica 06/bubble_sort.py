arreglo = [8,7,6,5,4,3,2,1]
contador = 0

for i in range(len(arreglo)-1):
    for j in range(len(arreglo)-1):
        num1 = arreglo[j]
        num2 = arreglo[j+1]
        if num1 > num2:
            arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        contador += 1
    print(arreglo)

print("Arreglo ordenado:", arreglo)
print("Número de comparaciones:", contador)