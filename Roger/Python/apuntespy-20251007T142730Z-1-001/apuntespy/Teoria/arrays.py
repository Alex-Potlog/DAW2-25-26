# 📌 Creación de Arrays (Listas en Python)
# Una lista puede almacenar múltiples valores de distintos tipos
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "María", "Carlos"]
mixta = [10, "Hola", 3.14, True]

# 📌 Acceso a Elementos
print(numeros[0])   # Primer elemento (1)
print(nombres[-1])  # Último elemento ("Carlos")
print(mixta[1:3])   # Slice (["Hola", 3.14])

# 📌 Modificación de Elementos
numeros[2] = 99  # Cambia el tercer elemento
print(numeros)

# 📌 Métodos de Listas
# Agregar y eliminar elementos
numeros.append(6)        # Agregar al final
numeros.insert(1, 100)   # Insertar en índice específico
numeros.remove(4)        # Eliminar la primera ocurrencia del valor
ultimo = numeros.pop()   # Elimina el último elemento y lo guarda
print(numeros)
print(f"Elemento eliminado con pop(): {ultimo}")

# 📌 Otras Operaciones con Listas
numeros.extend([7, 8, 9])  # Extiende la lista con otra
numeros.sort()             # Ordena la lista de menor a mayor
numeros.reverse()          # Invierte el orden de la lista
print(numeros)

# 📌 Búsqueda en Listas
print(numeros.index(100))   # Devuelve el índice del valor (si existe)
print(numeros.count(99))    # Cuenta cuántas veces aparece un valor

# 📌 Longitud de la Lista
print(f"Longitud de la lista: {len(numeros)}")

# 📌 Recorrer una Lista
print("Recorrido con for:")
for n in numeros:
    print(n)

print("Recorrido con while:")
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

# 📌 Listas por Comprensión
# Crear una nueva lista aplicando operaciones
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

# 📌 Copiar Listas
copia = numeros.copy()
print(f"Copia de la lista: {copia}")

# 📌 Vaciar la Lista
numeros.clear()
print(f"Lista vacía: {numeros}")

''' 
Comentario multi-línea:
Las listas son estructuras muy flexibles en Python.
Pueden crecer, reducirse y almacenar cualquier tipo de dato.
Los métodos son muy útiles para manipular los elementos.
'''
# 📌 Arrays Bidimensionales (Listas de Listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos
print(matriz[0][0])  # Primer fila, primer columna (1)
print(matriz[2][1])  # Tercer fila, segunda columna (8)

# Modificación de elementos
matriz[1][2] = 99    # Cambia el elemento en fila 2, columna 3
print(matriz)

# Recorrer la matriz con for anidado
print("Recorrido de la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea al final de cada fila

# Usando comprensión de listas para crear una matriz 3x3 de ceros
ceros = [[0 for _ in range(3)] for _ in range(3)]
print("Matriz de ceros:")
print(ceros)

# Agregar una fila o columna
nueva_fila = [10, 11, 12]
matriz.append(nueva_fila)  # Agrega al final
print("Matriz con nueva fila:")
print(matriz)

# Para agregar una columna, se debe recorrer cada fila
for i in range(len(matriz)):
    matriz[i].append(i+100)
print("Matriz con nueva columna:")
print(matriz)
