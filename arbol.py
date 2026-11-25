class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# Crear los nodos
raiz = Nodo(50)

raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)

raiz.izquierdo.izquierdo = Nodo(20)
raiz.izquierdo.derecho = Nodo(40)

raiz.derecho.izquierdo = Nodo(60)
raiz.derecho.derecho = Nodo(80)


# Recorrido en orden
def recorrer(nodo):
    if nodo is not None:
        recorrer(nodo.izquierdo)
        print(nodo.valor)
        recorrer(nodo.derecho)


print("Recorrido del árbol:")
recorrer(raiz)