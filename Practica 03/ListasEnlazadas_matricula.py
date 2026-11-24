class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.puntero = None
        
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
            while actual.puntero is not None:
                actual = actual.puntero
                
            actual.puntero = nuevo
            
    def mostrar(self):
        actual = self.head
    
        print("\n===== LISTA ENLAZADA =====")
        print("cabeza")
        print("  │")
        print("  ▼")
    
        while actual is not None:
            print(f"┌──────────┐")
            print(f"│   {actual.dato:<4}   │")
            if actual.puntero is not None:
                print(f"│ siguiente├─────►")
            else:
                print(f"│ siguiente├─────► None")
            print(f"└──────────┘")
    
            actual = actual.puntero
            
            
lista = lista()

lista.agregar(10)
lista.agregar(80)
lista.agregar(30)
lista.agregar(110)
lista.agregar(50)

lista.mostrar()