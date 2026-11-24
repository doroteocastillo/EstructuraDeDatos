class nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.dere = None

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izq)
        preorden(nodo.dere)

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izq)
        print(nodo.valor)
        inorden(nodo.dere)

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.dere)
        print(nodo.valor)

#NODO RAIZ
raiz = nodo(10)

#LADO IZQUIERDO DE LA RAIZ
raiz.izq = nodo(5)
#LADO DERECHO DE LA RAIZ
raiz.dere = nodo(20)

#LADO IZQUIERDO DEL LADO IZQ DE LA RAIZ
raiz.izq.izq = nodo(2)
raiz.izq.dere = nodo(7)

raiz.dere.izq = nodo(15)
raiz.dere.dere = nodo(30)

print("====RECORRIDO PREORDEN===")
preorden(raiz) #10,5,2,7,20,15,30
inorden(raiz) #2,5,7,10,15,20,30
postorden(raiz) #2,7,5,15,30,20,10