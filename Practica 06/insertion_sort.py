arreglo = [5, 8, 3, 2, 7, 6]

puntero1 = 0
puntero2=puntero1 + 1
intercambio = True
vueltas = 0

while vueltas < (len(arreglo)-1):
    for i in range(len(arreglo)-1):
        intercambio = False
        #Seleccionar el puntero1 del arreglo. Guardar en num1.
        num1 = arreglo[puntero1]

        #Seleccionar el puntero2 del arreglo. Guardar en num2.
        num2 = arreglo[puntero2]

        #comparamos num1>num2
        if num1 > num2:
            arreglo[puntero1], arreglo[puntero2] = arreglo[puntero2], arreglo[puntero1]
            intercambio = True
        #Si hubo intercambio
        if intercambio:
            #reiniciamos el ciclo y los punteros
            vueltas = 0
            puntero1 = 0
            puntero2 = puntero1 + 1
            break
        
        #Si no hubo intercambio, avanzamos los punteros
        puntero1 += 1
        puntero2 += 1
        vueltas += 1
print(arreglo)