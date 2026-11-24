from collections import deque

queue = deque()

# Agregar personas
queue.append("Ana")
queue.append("Luis")
queue.append("Pedro")
queue.append("María")

print("Queue:", list(queue))

# Atender a la primera persona
atendido = queue.popleft()

print("Persona atendida:", atendido)
print("Personas restantes:", list(queue))