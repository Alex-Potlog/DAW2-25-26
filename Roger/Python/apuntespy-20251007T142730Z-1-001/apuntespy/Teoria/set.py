# 📌 Creación de Sets
# Un set es una colección no ordenada y sin elementos duplicados
mi_set = {1, 2, 3, 4}
print(mi_set)   # {1, 2, 3, 4}

# 📌 Métodos de Sets
mi_set.add(5)        # Agregar elemento
mi_set.remove(2)     # Eliminar un elemento
mi_set.discard(99)   # Elimina sin error si no existe
ultimo = mi_set.pop()  # Elimina un elemento "cualquiera", !IMPORTNTE lo devuelve
print(mi_set)
print(f"Elemento eliminado con pop(): {ultimo}")

# 📌 Operaciones de Conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))         # Unión → {1,2,3,4,5,6}
print(a.intersection(b))  # Intersección → {3,4}
print(a.difference(b))    # Diferencia → {1,2}
print(a.symmetric_difference(b)) # Diferencia simétrica → {1,2,5,6}

# 📌 Verificación
print(3 in a)   # True
print(10 not in b)  # True

# 📌 Recorrer un Set
for valor in mi_set:
    print(valor)

# 📌 Crear Set desde Lista
lista = [1, 2, 2, 3, 4, 4, 5]
set_sin_duplicados = set(lista)
print(set_sin_duplicados)

''' 
Comentario multi-línea:
Los sets son ideales para trabajar con colecciones sin duplicados.
Muy útiles en operaciones matemáticas y filtrado de datos.
'''
