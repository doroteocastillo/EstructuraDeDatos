datos = list(range(1, 101))

#O(1)
print("=====O(1)=====")

def o1(lista):
    return lista[50]
    
print(o1(datos))

#O(log n)
print("=====O(log n)=====")
def on(lista):
    contador = 1
    objetivo = 22
    inicio = min(lista)
    fin = max(lista)
    while inicio <= fin:
        
        mitad = (inicio + fin) // 2
        print(f"la mitad es: {mitad}")
        
        if (mitad == objetivo):
            return contador
        elif (objetivo < mitad):
            fin = mitad - 1
        else:
            inicio = mitad + 1
            
        contador += 1
        
print(f"Número de contadores {on(datos)}")