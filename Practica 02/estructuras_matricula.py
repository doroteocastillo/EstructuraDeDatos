"""
ESTRUCTURAS LINEALES
    - Arreglos (arrays)
    - Listas
    - Pilas
    - Filas
"""

#===ARREGLOS===
print("==========ARREGLOS==========")
"""
Son de memoria estática
Tienen un índice, al buscar su información utilizan O(1)
"""

#CREATE
arreglo = [10,20,30,40,50]
#READ
print(arreglo)
print("El dato en la tercer posición es:", arreglo[2])
#UPDATE
arreglo[4] = 60
print(arreglo)
#DELETE
del arreglo[3]
print(arreglo)

#LISTAS DINÁMICAS O ENLAZADAS
"""
Comienzan con una cabecera (HEAD)
1. Lista simplemente relacionada
Cada nodo apunta al siguiente.
2. Lista doblemente enlazada
Cada nodo apunta al siguiente (next) y al pasado (prev)
3. Lista circular
El último nodo apunta al HEAD

INSERSION
La cabecera utiliza O(1)
Los nodos consecuentes O(n)
ELIMINACIÓN
En el HEAD O(1)
En los nodos consecuentes O(n)
BUSQUEDA O RECORRIDO
En el HEAD O(1)
En los nodos consecuentes O(n)
"""

#CREATE
print("==========LISTA DINÁMICA/ENLAZADA==========")
lista_din = []
lista_din.append("Jorge")
lista_din.append("Dannae")
lista_din.append("Diego")
#READ
print(lista_din)
#UPDATE
lista_din[1] = "Danae"
print(lista_din)
#DELETE
lista_din.remove("Jorge")
print(lista_din)

#PILAS / STACKS
"""
Funcionan con el principio LIFO
(Last in, First Out)

TIENEN UN PUNTERO back

Agregar implica un O(1), alfinal.
Eliminar implica un O(1), al final.
"""
print("==========STACKS==========")

#CREATE
stack = [10,20,30,40]
#READ
print(stack)
#UPDATE
stack.append(50)
stack.append(60)
print(stack)
#DELETE
stack.pop()
print(stack)

print("==========HEAPS==========")
"""
Funcionan con el principio de FIFO
(First in, First Out)

Las queue se señalan por 2 punteros
Front y Rear/back

AGREGAR/Enqueue
Generas un dato en el back - O(1)

ELIMINAR/Dequeue
Remueve el elemento en el front - O(1)

"""
#CREATE
heaps = [10,20,30]
#READ
print(heaps)
#UPDATE
heaps.append(40)
print(heaps)
#DELETE
del heaps[0]
heaps.append(50)
del heaps[0]
print(heaps)

print("==========ÁRBOL BINARIO==========")
"""
Python trabaja con diccionarios
un diccionario almaneca informacion en datos
parecidos a JSON
"""
#CREATE
arbol={
    "valor":10,
    "izquierda":{
        "valor":20,
        "izquierda":40,
        "derecha":50
    },
    "derecha":{
        "valor":30,
        "izquierda":60,
        "derecha":70
    },
    "centro":80
}
#READ
print(arbol)
#UPDATE
arbol["derecha"]["izquierda"] = 90
print(arbol)
#DELETE
del arbol["izquierda"]["derecha"]
print(arbol)

print("==========TABLA HASH==========")
"""
Trabaja igualmente con diccionarios
"""
#CREATE
alumnos = {
    "Mariano":9.2,
    "Alvaro":8.2,
    "Santiago":9.4
}
#READ
print(alumnos)
print(f"Alvaro obtuvo {alumnos['Alvaro']}")
#UPDATE
alumnos["Mariano"]=9.4
print(f"Mariano despues de cambiar obtuvo {alumnos['Mariano']}")
#DELETE
del alumnos["Santiago"]
print(alumnos)