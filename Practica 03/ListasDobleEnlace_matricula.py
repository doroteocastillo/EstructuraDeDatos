import random as r

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class lista:
    def __init__(self):
        self.head = None
        
    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            """mientras su puntero no apunte a null
            eso quieres decir que el nodo actual no es el ultimo"""
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

    def mostrar(self):
        actual = self.head

        print("\n===== LISTA DOBLEMENTE ENLAZADA =====")
        print("cabeza")
        print("  │")
        print("  ▼")

        while actual is not None:
            anterior = actual.anterior.dato if actual.anterior is not None else "None"
            siguiente = actual.siguiente.dato if actual.siguiente is not None else "None"

            print("┌─────────────────────┐")
            print(f"│ anterior:  {anterior:<7} │")
            print(f"│ dato:      {actual.dato:<7} │")
            print(f"│ siguiente: {siguiente:<7} │")
            print("└─────────────────────┘")

            if actual.siguiente is not None:
                print("          ↕")
            else:
                print("          │")
                print("         None")

            actual = actual.siguiente

    def buscar(self, busqueda):
        contador = 1
        actual = self.head
        while actual is not None:
            if busqueda == actual.dato:
                print(f"DATO {busqueda} ENCONTRADO")
                print(f"NUMERO DE CONTEOS: {contador}")
                return
            else:
                actual = actual.siguiente
                contador +=1
        print(f"DATO {busqueda} NO HA SIDO ENCONTRADO")
        print(f"NUMERO DE CONTEOS: {contador-1}")


lista = lista()

for numero in r.sample(range(1, 1001), 100):
    lista.agregar(numero)

lista.buscar(342)
