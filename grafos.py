grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}

# Mostrar conexiones
for edificio, conexiones in grafo.items():
    print(edificio, "conecta con:", conexiones)