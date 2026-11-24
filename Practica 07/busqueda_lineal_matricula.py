datos = [
    '3658', '5367', '7844', '5235', '5219', '0770', '0478', '4451', '5044', '5075', '4709'
]

#SOLICITAMOS AL USUARIO QUE MATRICULA BUSCA. GUARDAR EN 'busqueda'
#SOLICITAR/PEDIR/REQUERIR → → → → input
#¿QUE MATRICULA BUSCA? → → → → → TEXTO

busqueda = input("¿Qué matricula buscas? ")
encontrado = False
contador = 0

"""BUSCAR EN EL ARREGLO EL VALOR"""
#RECORREMOS CON UN for TODO EL ARREGLO
for i in range(len(datos)): #len nos devuelve un int del tamaño del arreglo

    #AUMENTAMOS EL CONTADOR EN 1 CON CADA VUELTA
    contador += 1


    #EN CADA VUELTA, COMPARA QUE LO QUE BUSQUE SEA IGUAL AL VALOR DENTRO DEL CAJÓN
    #COMPARAR → → → if
    if busqueda == datos[i]:
        #ESCRIBIR QUE EL DATO HA SIDO ENCONTRADO:
        #ESCRIBIR → → → print
        print("El dato ha sido encontrado")
        encontrado = True
        break #break ROMPE CUALQUIER CICLO EN EL QUE ESTÉ


if not encontrado:
    print("No se encontró la matricula.")

print("Numero de vueltas:", contador)