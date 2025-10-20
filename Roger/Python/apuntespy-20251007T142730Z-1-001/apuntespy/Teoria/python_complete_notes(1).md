# Apuntes Completos de Python

## 📚 Índice
1. [Arrays (Listas)](#arrays-listas)
2. [Condicionales](#condicionales)
3. [Función map()](#función-map)
4. [Diccionarios](#diccionarios)

---

## 📌 Arrays (Listas)

### Creación de Listas
```python
# Listas simples
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "María", "Carlos"]
mixta = [10, "Hola", 3.14, True]
vacia = []
```

### Acceso a Elementos
```python
numeros = [1, 2, 3, 4, 5]

print(numeros[0])    # Primer elemento → 1
print(numeros[-1])   # Último elemento → 5
print(numeros[-2])   # Penúltimo elemento → 4
print(numeros[1:3])  # Slice [inicio:fin) → [2, 3]
print(numeros[:3])   # Desde inicio hasta índice 3 → [1, 2, 3]
print(numeros[2:])   # Desde índice 2 hasta el final → [3, 4, 5]
```

### Modificación de Elementos
```python
numeros = [1, 2, 3, 4, 5]
numeros[2] = 99     # Cambia el tercer elemento
print(numeros)      # [1, 2, 99, 4, 5]
```

### Métodos Principales de Listas

#### Agregar elementos
```python
lista = [1, 2, 3]

lista.append(4)         # Agregar al final → [1, 2, 3, 4]
lista.insert(1, 100)    # Insertar en índice 1 → [1, 100, 2, 3, 4]
lista.extend([5, 6])    # Extender con otra lista → [1, 100, 2, 3, 4, 5, 6]
```

#### Eliminar elementos
```python
lista = [1, 2, 3, 4, 5, 3]

lista.remove(3)         # Elimina primera ocurrencia de 3 → [1, 2, 4, 5, 3]
ultimo = lista.pop()    # Elimina y devuelve el último → [1, 2, 4, 5]
elemento = lista.pop(1) # Elimina y devuelve índice 1 → [1, 4, 5]
del lista[0]            # Elimina elemento en índice 0 → [4, 5]
lista.clear()           # Vacía completamente la lista → []
```

#### Ordenar y manipular
```python
numeros = [5, 2, 8, 1, 9]

numeros.sort()          # Ordena ascendente → [1, 2, 5, 8, 9]
numeros.sort(reverse=True)  # Ordena descendente → [9, 8, 5, 2, 1]
numeros.reverse()       # Invierte el orden actual
```

#### Búsqueda y conteo
```python
lista = [1, 2, 3, 2, 4, 2]

indice = lista.index(3)     # Devuelve índice del valor 3 → 2
cantidad = lista.count(2)   # Cuenta ocurrencias de 2 → 3
existe = 5 in lista         # Comprueba si existe → False
longitud = len(lista)       # Longitud de la lista → 6
```

### Recorrer Listas

#### Con for
```python
numeros = [1, 2, 3, 4, 5]

# Recorrer valores
for numero in numeros:
    print(numero)

# Recorrer con índice
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")

# Recorrer con enumerate (mejor práctica)
for i, numero in enumerate(numeros):
    print(f"Índice {i}: {numero}")
```

#### Con while
```python
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
```

### Listas por Comprensión
```python
# Crear lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]
# Resultado: [1, 4, 9, 16, 25]

# Con condición
pares = [x for x in range(10) if x % 2 == 0]
# Resultado: [0, 2, 4, 6, 8]

# Transformación
palabras = ["hola", "mundo", "python"]
mayusculas = [p.upper() for p in palabras]
# Resultado: ['HOLA', 'MUNDO', 'PYTHON']
```

### Copiar Listas
```python
original = [1, 2, 3]

# ⚠️ NO hacer esto (copia la referencia)
copia_mal = original
copia_mal[0] = 99  # ¡Modifica el original también!

# ✅ Formas correctas de copiar
copia1 = original.copy()
copia2 = original[:]
copia3 = list(original)
```

### Arrays Bidimensionales (Matrices)
```python
# Crear matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos
print(matriz[0][0])  # Fila 0, Columna 0 → 1
print(matriz[2][1])  # Fila 2, Columna 1 → 8

# Modificar elemento
matriz[1][2] = 99

# Recorrer matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila

# Recorrer con índices
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"[{i}][{j}] = {matriz[i][j]}")

# Crear matriz con comprensión
ceros = [[0 for _ in range(3)] for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 🔀 Condicionales

### Estructura if-elif-else
```python
x = int(input("Escoge un número: "))

if x < 0:
    print(f"{x} es negativo")
elif x > 0:
    print(f"{x} es positivo")
else:  # x == 0
    print(f"{x} es cero")
```

### Operadores de Comparación
```python
==  # Igual a
!=  # Diferente de
<   # Menor que
>   # Mayor que
<=  # Menor o igual que
>=  # Mayor o igual que
```

### Operadores Lógicos
```python
# ⚠️ IMPORTANTE: En Python se usa 'and', 'or', 'not'
# NO se usan &, |, ! para lógica booleana

nota = 7

# ✅ Correcto
if nota >= 5 and nota < 7:
    print("Aprobado")

# ❌ Incorrecto (& es para operaciones bit a bit)
if nota >= 5 & nota < 7:  # ¡No funciona como esperas!
    print("Aprobado")
```

### Ejemplos de Operadores Lógicos
```python
# AND (ambas condiciones deben ser True)
x = 5
if x > 0 and x < 10:
    print("x está entre 0 y 10")

# OR (al menos una condición debe ser True)
if x == 5 or x == 10:
    print("x es 5 o 10")

# NOT (invierte el valor booleano)
if not (x < 0):
    print("x no es negativo")

# Combinación
edad = 20
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puede conducir")
```

### Ejemplo Completo: Sistema de Notas
```python
nota = float(input("Introduce tu nota (0-10): "))

if nota < 0 or nota > 10:
    print("Error: nota fuera de rango")
elif nota < 5:
    print(f"{nota}: Suspendido")
elif nota < 7:
    print(f"{nota}: Aprobado")
elif nota < 9:
    print(f"{nota}: Notable")
else:  # nota >= 9
    print(f"{nota}: Sobresaliente")
```

### Condicionales en una Línea
```python
# Operador ternario
edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

# Equivalente a:
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"
```

---

## 🗺️ Función map()

### Concepto Básico
`map()` aplica una función a cada elemento de un iterable y devuelve un objeto map.

### Sintaxis
```python
map(función, iterable)
```

### Ejemplos Básicos

#### Convertir tipos
```python
# Strings a enteros
numeros_str = ["1", "2", "3", "4"]
numeros_int = list(map(int, numeros_str))
# Resultado: [1, 2, 3, 4]

# Enteros a strings
numeros = [1, 2, 3]
strings = list(map(str, numeros))
# Resultado: ['1', '2', '3']
```

#### Con funciones propias
```python
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
cuadrados = list(map(cuadrado, numeros))
# Resultado: [1, 4, 9, 16]
```

#### Con funciones lambda
```python
# Duplicar valores
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
# Resultado: [2, 4, 6, 8]

# Formatear strings
nombres = ["ana", "luis", "maría"]
capitalizados = list(map(lambda s: s.capitalize(), nombres))
# Resultado: ['Ana', 'Luis', 'María']
```

### Uso Común: Lectura de Entrada
```python
# Leer múltiples números en una línea
entrada = "10 20 30 40 50"
numeros = list(map(int, entrada.split()))
# Resultado: [10, 20, 30, 40, 50]

# Aplicado directamente a input()
# Entrada del usuario: "5 10 15"
valores = list(map(int, input("Números: ").split()))
```

### Map con Múltiples Iterables
```python
# Sumar dos listas elemento por elemento
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
suma = list(map(lambda x, y: x + y, lista1, lista2))
# Resultado: [11, 22, 33]
```

### Comparación: map() vs list comprehension
```python
numeros = [1, 2, 3, 4]

# Con map()
cuadrados1 = list(map(lambda x: x**2, numeros))

# Con list comprehension (más pythónico)
cuadrados2 = [x**2 for x in numeros]

# Ambos dan: [1, 4, 9, 16]
```

---

## 📖 Diccionarios

### Creación de Diccionarios
```python
# Diccionario vacío
vacio = {}
vacio2 = dict()

# Con valores iniciales
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Desde listas
claves = ["a", "b", "c"]
valores = [1, 2, 3]
diccionario = dict(zip(claves, valores))
# {'a': 1, 'b': 2, 'c': 3}
```

### Acceso a Valores

#### Acceso directo
```python
persona = {"nombre": "Ana", "edad": 25}

# ✅ Si existe la clave
print(persona["nombre"])  # Ana

# ❌ Si no existe → KeyError
try:
    print(persona["apellido"])
except KeyError:
    print("La clave no existe")
```

#### Acceso seguro con get()
```python
# Devuelve None si no existe
apellido = persona.get("apellido")  # None

# Con valor por defecto
apellido = persona.get("apellido", "Desconocido")  # Desconocido
edad = persona.get("edad", 0)  # 25
```

### Añadir y Modificar
```python
persona = {"nombre": "Ana"}

# Añadir nueva clave
persona["edad"] = 25
persona["ciudad"] = "Barcelona"

# Modificar valor existente
persona["nombre"] = "María"

print(persona)
# {'nombre': 'María', 'edad': 25, 'ciudad': 'Barcelona'}
```

### Eliminar Elementos
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Eliminar con del
del persona["ciudad"]

# Eliminar con pop() (devuelve el valor)
edad = persona.pop("edad")  # 25

# pop() con valor por defecto si no existe
telefono = persona.pop("telefono", "No disponible")

# Eliminar todos los elementos
persona.clear()
```

### Comprobar Existencia
```python
persona = {"nombre": "Ana", "edad": 25}

# Comprobar si existe una clave
if "nombre" in persona:
    print("La clave 'nombre' existe")

if "apellido" not in persona:
    print("La clave 'apellido' NO existe")
```

### Métodos Principales

#### keys(), values(), items()
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}

# Obtener todas las claves
claves = persona.keys()
# dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener todos los valores
valores = persona.values()
# dict_values(['Ana', 25, 'Barcelona'])

# Obtener pares clave-valor
items = persona.items()
# dict_items([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Barcelona')])

# Convertir a lista
lista_claves = list(persona.keys())  # ['nombre', 'edad', 'ciudad']
```

### Recorrer Diccionarios

#### Recorrer claves
```python
for clave in persona:
    print(clave)
# nombre
# edad
# ciudad
```

#### Recorrer valores
```python
for valor in persona.values():
    print(valor)
# Ana
# 25
# Barcelona
```

#### Recorrer claves y valores
```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# nombre: Ana
# edad: 25
# ciudad: Barcelona
```

### Ejemplos Prácticos

#### Contar frecuencias (método básico)
```python
texto = "abracadabra"
frecuencia = {}

for letra in texto:
    if letra in frecuencia:
        frecuencia[letra] = frecuencia[letra] + 1
    else:
        frecuencia[letra] = 1

print(frecuencia)
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

#### Contar frecuencias (con get)
```python
texto = "abracadabra"
frecuencia = {}

for letra in texto:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1

print(frecuencia)
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

#### Agrupar elementos
```python
# Agrupar alumnos por clase
alumnos = [
    ("Ana", "1A"),
    ("Luis", "1B"),
    ("María", "1A"),
    ("Carlos", "1B")
]

clases = {}
for nombre, clase in alumnos:
    if clase in clases:
        clases[clase].append(nombre)
    else:
        clases[clase] = [nombre]

print(clases)
# {'1A': ['Ana', 'María'], '1B': ['Luis', 'Carlos']}
```

#### Agrupar con get()
```python
clases = {}
for nombre, clase in alumnos:
    clases[clase] = clases.get(clase, []) + [nombre]

print(clases)
# {'1A': ['Ana', 'María'], '1B': ['Luis', 'Carlos']}
```

#### Diccionario de diccionarios
```python
estudiantes = {
    "001": {"nombre": "Ana", "nota": 8.5},
    "002": {"nombre": "Luis", "nota": 7.0},
    "003": {"nombre": "María", "nota": 9.5}
}

# Acceso
print(estudiantes["001"]["nombre"])  # Ana
print(estudiantes["002"]["nota"])    # 7.0

# Modificar
estudiantes["001"]["nota"] = 9.0
```

### Operaciones Avanzadas

#### Fusionar diccionarios
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.9+
fusion = dict1 | dict2
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Alternativa (todas las versiones)
fusion = {**dict1, **dict2}

# Método update (modifica el original)
dict1.update(dict2)
```

#### Diccionario por comprensión
```python
# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condición
pares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### Tabla Resumen - Diccionarios

| Operación | Código | Descripción |
|-----------|--------|-------------|
| Crear vacío | `d = {}` | Diccionario vacío |
| Crear con datos | `d = {"a": 1, "b": 2}` | Con pares clave:valor |
| Acceder | `d["a"]` | Acceso directo (KeyError si no existe) |
| Acceder seguro | `d.get("a", 0)` | Con valor por defecto |
| Añadir/modificar | `d["c"] = 3` | Añade o modifica |
| Comprobar | `"a" in d` | True si la clave existe |
| Eliminar | `del d["a"]` | Elimina la clave |
| Pop | `d.pop("a", None)` | Elimina y devuelve el valor |
| Claves | `d.keys()` | Todas las claves |
| Valores | `d.values()` | Todos los valores |
| Items | `d.items()` | Pares (clave, valor) |
| Vaciar | `d.clear()` | Elimina todo |
| Longitud | `len(d)` | Número de elementos |

### Consejos Importantes

1. **Usa `get()` para evitar errores**: Especialmente cuando no estás seguro si una clave existe
2. **Las claves deben ser inmutables**: Strings, números, tuplas (NO listas)
3. **Los valores pueden ser cualquier cosa**: Listas, otros diccionarios, objetos, etc.
4. **Diccionarios no tienen orden garantizado** (antes de Python 3.7)
5. **Desde Python 3.7+**: Los diccionarios mantienen el orden de inserción

---

## 🎯 Resumen de Mejores Prácticas

### Listas
- Usa `enumerate()` en lugar de `range(len())` al recorrer con índices
- Prefiere list comprehension sobre `map()` para operaciones simples
- Copia listas con `.copy()` o `[:]` para evitar modificar el original

### Condicionales
- Usa `and`, `or`, `not` (NO `&`, `|`, `!`)
- Mantén las condiciones simples y legibles
- Considera el operador ternario para asignaciones simples

### Map
- Útil para conversiones de tipo masivas
- Considera list comprehension para mayor legibilidad
- Perfecto para transformaciones de entrada del usuario

### Diccionarios
- Usa `get()` con valor por defecto para evitar KeyError
- Recorre con `.items()` cuando necesites clave y valor
- Inicializa valores complejos (listas, diccionarios) con `get()`