# 📌 Creación de Tuplas
# Una tupla es una colección ordenada e inmutable
tupla1 = (1, 2, 3, 4, 5)
tupla2 = ("Ana", "Luis", "María", "Carlos")
mixta = (10, "Hola", 3.14, True)

# 📌 Acceso a Elementos
print(tupla1[0])     # Primer elemento (1)
print(tupla2[-1])    # Último elemento ("Carlos")
print(mixta[1:3])    # Slice ("Hola", 3.14)

# 📌 Inmutabilidad
# tupla1[0] = 99  ❌ Esto da error, no se pueden modificar elementos

# 📌 Operaciones con Tuplas
print(len(tupla1))         # Longitud de la tupla
print(tupla1.count(2))     # Contar ocurrencias
print(tupla1.index(3))     # Obtener índice de un valor

# 📌 Recorrer una Tupla
print("Recorrido con for:")
for elemento in tupla2:
    print(elemento)

# 📌 Desempaquetado de Tuplas
x, y, z = (1, 2, 3)
print(x, y, z)

# 📌 Tuplas Anidadas
anidada = (1, (2, 3), (4, 5))
print(anidada[1][0])   # 2

''' 
Comentario multi-línea:
Las tuplas son útiles para datos fijos que no deben cambiar.
Se usan mucho para coordenadas, registros o retornos múltiples de funciones.
'''
