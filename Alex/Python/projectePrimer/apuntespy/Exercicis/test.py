# 📌 Uso de Variables y Conversión de Tipos
# Solicitamos al usuario dos números y los convertimos a enteros
x = int(input("Escoge un número: "))  # Conversión de entrada a entero
y = int(input("Escoge otro número: "))  # Conversión de entrada a entero

# 📌 Operaciones Matemáticas
# Realizamos varias operaciones con los números ingresados
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y  # División con decimales
division_entera = x // y  # División entera
modulo = x % y  # Resto de la división
potencia = x ** y  # Potencia

# 📌 Impresión de Resultados
# Imprimimos los resultados usando diferentes métodos
print("Resultados de las operaciones:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División (float): {division:.2f}")  # Imprime con 2 decimales
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")

# 📌 Comparadores
# Comparamos los valores ingresados
print("Comparaciones entre x e y:")
print(f"x == y: {x == y}")  # Igualdad
print(f"x != y: {x != y}")  # Desigualdad
print(f"x > y: {x > y}")    # Mayor que
print(f"x < y: {x < y}")    # Menor que
print(f"x >= y: {x >= y}")  # Mayor o igual
print(f"x <= y: {x <= y}")  # Menor o igual

# 📌 Estructuras de Control
# Usamos condicionales para evaluar la relación entre x e y
if x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual a y")
else:
    print("x es menor que y")

# 📌 Bucles
# Bucle for: imprime los números del 0 al x-1
print("Bucle for:")
for i in range(x):
    print(f"Iteración {i}")

# Bucle while: cuenta hasta y
print("Bucle while:")
contador = 0
while contador < y:
    print(f"Contador: {contador}")
    contador += 1

# 📌 Comentarios
# Comentario de una línea
# Este es un comentario simple

''' 
Comentario multi-línea
Este bloque puede contener explicaciones más extensas
sobre el código o documentación interna.
'''

# 📌 Mostrar tipo de variable
print(f"Tipo de variable x: {type(x)}")
print(f"Tipo de variable division: {type(division)}")