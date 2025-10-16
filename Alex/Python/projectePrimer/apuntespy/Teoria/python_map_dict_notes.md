# Apuntes de Python: map() y Diccionarios

## 1. Función map()

### ¿Qué es map()?
`map()` es una función que aplica otra función a cada elemento de un iterable (lista, tupla, etc.) y devuelve un objeto map (que podemos convertir a lista).

### Sintaxis básica
```python
map(función, iterable)
```

### Ejemplos de uso

#### Ejemplo 1: Convertir strings a enteros
```python
numeros_str = ["1", "2", "3", "4"]
numeros_int = list(map(int, numeros_str))
# Resultado: [1, 2, 3, 4]
```

#### Ejemplo 2: Aplicar una función personalizada
```python
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
cuadrados = list(map(cuadrado, numeros))
# Resultado: [1, 4, 9, 16]
```

#### Ejemplo 3: Con funciones lambda
```python
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
# Resultado: [2, 4, 6, 8]
```

#### Ejemplo 4: Uso común con split()
```python
# Convertir una frase de números en lista de enteros
frase = "10 20 30 40"
lista = list(map(int, frase.split(" ")))
# Resultado: [10, 20, 30, 40]
```

### Ventajas de map()
- Código más limpio y conciso
- Más eficiente que un bucle for en algunos casos
- Funcional y fácil de leer

---

## 2. Diccionarios (dict)

### ¿Qué es un diccionario?
Un diccionario es una estructura de datos que almacena pares **clave:valor**. Es como una lista pero accedemos a los elementos por una clave en lugar de por índice.

### Sintaxis básica
```python
# Crear un diccionario vacío
mi_dict = {}
mi_dict = dict()

# Crear con valores
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Barcelona"
}
```

### Operaciones básicas

#### Acceder a valores
```python
persona = {"nombre": "Ana", "edad": 25}

# Acceso directo
print(persona["nombre"])  # Ana

# Acceso seguro con get() (no da error si no existe)
print(persona.get("nombre"))  # Ana
print(persona.get("apellido", "No disponible"))  # No disponible
```

#### Añadir o modificar elementos
```python
persona = {"nombre": "Ana"}

# Añadir nuevo par clave-valor
persona["edad"] = 25

# Modificar valor existente
persona["nombre"] = "María"

print(persona)  # {"nombre": "María", "edad": 25}
```

#### Comprobar si existe una clave
```python
persona = {"nombre": "Ana", "edad": 25}

if "nombre" in persona:
    print("La clave existe")

if "apellido" not in persona:
    print("La clave no existe")
```

#### Eliminar elementos
```python
persona = {"nombre": "Ana", "edad": 25}

# Eliminar con del
del persona["edad"]

# Eliminar con pop() (devuelve el valor)
edad = persona.pop("edad", None)
```

### Métodos útiles de diccionarios

#### keys(), values(), items()
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}

# Obtener todas las claves
claves = persona.keys()  # dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener todos los valores
valores = persona.values()  # dict_values(['Ana', 25, 'Barcelona'])

# Obtener pares clave-valor
items = persona.items()  # dict_items([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Barcelona')])
```

#### get() con valor por defecto
```python
persona = {"nombre": "Ana"}

# Si la clave no existe, devuelve el valor por defecto
edad = persona.get("edad", 0)  # 0
nombre = persona.get("nombre", "Desconocido")  # Ana
```

### Recorrer diccionarios

#### Recorrer claves
```python
persona = {"nombre": "Ana", "edad": 25}

for clave in persona:
    print(clave)
# nombre
# edad
```

#### Recorrer valores
```python
for valor in persona.values():
    print(valor)
# Ana
# 25
```

#### Recorrer claves y valores
```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
# nombre: Ana
# edad: 25
```

### Ejemplos prácticos

#### Ejemplo 1: Contar frecuencias
```python
letras = "abracadabra"
frecuencia = {}

for letra in letras:
    if letra in frecuencia:
        frecuencia[letra] = frecuencia[letra] + 1
    else:
        frecuencia[letra] = 1

print(frecuencia)
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

#### Ejemplo 2: Con get() (más elegante)
```python
letras = "abracadabra"
frecuencia = {}

for letra in letras:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1

print(frecuencia)
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

#### Ejemplo 3: Diccionario con listas como valores
```python
grupos = {}
alumnos = [("Ana", "A"), ("Pedro", "B"), ("Luis", "A"), ("María", "B")]

for nombre, grupo in alumnos:
    if grupo in grupos:
        grupos[grupo].append(nombre)
    else:
        grupos[grupo] = [nombre]

print(grupos)
# {'A': ['Ana', 'Luis'], 'B': ['Pedro', 'María']}
```

#### Ejemplo 4: Con get() y listas
```python
grupos = {}

for nombre, grupo in alumnos:
    grupos[grupo] = grupos.get(grupo, []) + [nombre]

print(grupos)
# {'A': ['Ana', 'Luis'], 'B': ['Pedro', 'María']}
```

### Diferencias entre acceso directo y get()

```python
persona = {"nombre": "Ana"}

# Acceso directo - da error si no existe
try:
    edad = persona["edad"]
except KeyError:
    print("¡Error! La clave no existe")

# Con get() - devuelve None o un valor por defecto
edad = persona.get("edad")  # None
edad = persona.get("edad", 0)  # 0
```

### Trucos y consejos

1. **Usa get() para evitar errores**: Cuando no estés seguro si una clave existe.
2. **Inicialización elegante**: `dict.get(clave, valor_inicial)` es muy útil para contadores y acumuladores.
3. **Diccionarios con valores complejos**: Puedes tener listas, otros diccionarios, tuplas, etc. como valores.
4. **Claves inmutables**: Las claves deben ser inmutables (strings, números, tuplas), no pueden ser listas.

### Resumen rápido

| Operación | Código | Descripción |
|-----------|--------|-------------|
| Crear vacío | `d = {}` | Diccionario vacío |
| Crear con datos | `d = {"a": 1}` | Con par clave:valor |
| Acceder | `d["a"]` | Acceso directo (puede dar error) |
| Acceder seguro | `d.get("a", 0)` | Con valor por defecto |
| Añadir/modificar | `d["b"] = 2` | Añade o modifica |
| Comprobar existencia | `"a" in d` | Devuelve True/False |
| Eliminar | `del d["a"]` | Elimina la clave |
| Obtener claves | `d.keys()` | Todas las claves |
| Obtener valores | `d.values()` | Todos los valores |
| Obtener items | `d.items()` | Pares (clave, valor) |