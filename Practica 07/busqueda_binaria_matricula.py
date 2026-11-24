"""
CREAR LOS DATOS
DEBEN ESTAR ORDENADO DE MAYOR A MENOR

1. SOLICITAR EL NUMERO QUE BUSCAS. GUARDAR EN busqueda
2. ENCONTRAR EL ELEMENTO CENTRAL.
    SE CALCULA CON medio = (inicio + fin) // 2
3. COMPARAMOS busqueda CON medio
    4. SI ES IGUAL. TERMINAMOS LA BUSQUEDA.
5. SI NO. COMPARAMOS busqueda MAYOR QUE medio
    SI ES MAYOR. TOMAMOS LA PARTE DERECHA
    SI NO. TOMAMOS LA PARTE IZQUIERDA
"""

import random

datos = sorted(random.sample(range(10000), 10000))
datos = [f"{numero:04d}" for numero in datos]

inicio = 0
final = len(datos)
contador = 0
encontrado = False

def tomar_derecha():
    global inicio
    inicio = medio + 1

def tomar_izquierda():
    global final
    final = medio - 1

#1
busqueda = input("¿Qué matricula buscas? ")

while inicio <= final:
    contador += 1
    #2
    medio = (inicio + final) // 2

    #3
    if busqueda == datos[medio]:
        #4
        print("Dato encotrado")
        encontrado = True
        break

    #5
    elif int(busqueda) > int(datos[medio]):
        tomar_derecha()
    else:
        tomar_izquierda()

if not encontrado:
    print("Dato no registrado")

print("Número de operaciones:", contador)