# 📌 Creación de Diccionarios
# Un diccionario almacena pares clave-valor
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
#Forma similar a lo que podemos encontrar en php


# 📌 Acceso a Valores
print(persona["nombre"])     # Ana
print(persona.get("edad"))   # 25
print(persona.get("pais", "No existe"))  # Valor por defecto, lo mismo que ?? 'defecto'
# .get permite evitar KeyError, en caso de hacer persona["nombre"], si este no existe, BOOOMB


# 📌 Modificación y Agregado
persona["edad"] = 26
persona["profesion"] = "Ingeniera"
print(persona)
#Sencillo


# 📌 Eliminar Elementos
persona.pop("ciudad")     # Elimina una clave
ultima = persona.popitem() # Elimina el último par
print(f"Último par eliminado: {ultima}")
print(persona)


# 📌 Métodos Útiles
print(persona.keys())    # Claves
print(persona.values())  # Valores
print(persona.items())   # Pares clave-valor

# 📌 Recorrer un Diccionario / Array asociativo
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
#Mismo que PHP


# 📌 Diccionarios Anidados
alumnos = {
    "A1": {"nombre": "Luis", "edad": 20},
    "A2": {"nombre": "María", "edad": 22}
}
#Siempre se pueden hacer estructuras complejas, con diccionarios dentro de diccionarios

print(alumnos["A1"]["nombre"])  # Luis

# 📌 Crear Diccionario con dict()
dic = dict(id=1, nombre="Carlos", activo=True)
print(dic)

''' 
Comentario multi-línea:
Los diccionarios son de las estructuras más poderosas en Python.
Permiten modelar datos como "clave → valor" y son muy eficientes en búsquedas.
'''
