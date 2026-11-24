#GENERAR EL GRAFO

grafo = {
    'A' : ['B','C'],
    'B' : ['A','D'],
    'C' : ['A','D','E'],
    'D' : ['B','C','F'],
    'E' : ['C','F','G'],
    'F' : ['D','E','G'],
    'G' : ['E','F']
}

def buscar_ruta(origen, destino, grafo):
    queue = [origen]
    visitados = {origen}
    anterior = {origen:None}
    while queue:
        actual = queue.pop(0)
        if actual == destino:
            break
        
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                anterior[vecino] = actual
                queue.append(vecino)
    if destino not in visitados:
        return None
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = anterior[actual]
    ruta.reverse()
    return ruta
"""
El BFS funciona con el principio FIFO, utiliza una Queue
1. Coloca el origen en la Queue.
2. Marca el origen como visitado.
3. Extrae una estacion de las relaciones.
4. Examina las estaciones vecinas.
5. Si llegó al destino, contruye la ruta.
6. Comprueba que no haya sido visitado antes.
7. Si no, registra como visitado, coloca la estacion en la Queue y repite.
"""

for estacion, conexiones in grafo.items():
    print(estacion, "→", conexiones)

while True:
    origen = input("¿Desde dónde sales? ").upper()
    destino = input("¿A dónde quieres llegar?: ").upper()

#SI EL USUARIO COLOCA UN TEXTO O UNA LETRA QUE NO SEA DE LA A A LA G:
    if origen not in grafo or destino not in grafo:
        print("ERROR: Selecciona una estación válida")
        continue

#SI EL USUARIO COLOCA EL DESTINO Y EL ORIGEN IGUALES
    if origen == destino:
        print("Ya te encuentras en esa estación")
        continue
    
    print("Consultando ruta ...")

    ruta = buscar_ruta(origen, destino, grafo)
    
    if ruta is None:
        print("No existe ruta entre esas estaciones.")
    else:
        print("Ruta encontrada:")
        print("→".join(ruta))
        print("Numero de conexiones: ", len(ruta))