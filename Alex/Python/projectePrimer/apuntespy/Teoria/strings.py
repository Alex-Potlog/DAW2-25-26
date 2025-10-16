# 📌 Creación de Strings
cadena1 = "Hola mundo"
cadena2 = 'Python es genial'
cadena3 = """Este es un string
con varias líneas"""
cadena4 = "12345"

# 📌 Acceso a Caracteres
print(cadena1[0])   # Primer carácter: "H"
print(cadena1[-1])  # Último carácter: "o"
print(cadena1[0:4]) # Slice: "Hola"

# 📌 Concatenación y Repetición
saludo = "Hola " + "Python"
eco = "Hey! " * 3
print(saludo)
print(eco)

# 📌 Métodos de Strings (Manipulación)
texto = "  Bienvenido a Python  "

print(texto.upper())     # MAYÚSCULAS
print(texto.lower())     # minúsculas
print(texto.title())     # Tipo Título
print(texto.strip())     # Elimina espacios al inicio y fin
print(texto.replace("Python", "Java"))  # Reemplazo

# 📌 Búsqueda en Strings
print(texto.find("Python"))   # Devuelve el índice donde aparece
print(texto.count("e"))       # Cuenta cuántas veces aparece
print("Python" in texto)      # Verifica si contiene la palabra
print("Java" not in texto)    # Verifica si NO contiene la palabra

# 📌 División y Unión de Strings
frase = "uno,dos,tres,cuatro"
lista = frase.split(",")  # Convierte string en lista
print(lista)

nueva_frase = "-".join(lista)  # Une lista en un string
print(nueva_frase)

# 📌 Formateo de Strings
nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años")  # f-string
print("Me llamo {} y tengo {} años".format(nombre, edad))  # .format()

# 📌 Recorrer un String
print("Recorriendo string con for:")
for letra in nombre:
    print(letra)

print("Recorriendo string con while:")
i = 0
while i < len(nombre):
    print(nombre[i])
    i += 1

# 📌 Propiedades de Strings
print(len(cadena1))   # Longitud
print(cadena4.isdigit())  # Verifica si todos los caracteres son números
print(cadena1.isalpha())  # Verifica si son solo letras
print("python".startswith("py"))  # Comienza con
print("python".endswith("on"))    # Termina con

# 📌 Substrings
mensaje = "Aprendiendo Python paso a paso"
print(mensaje[0:11])   # "Aprendiendo"
print(mensaje[-4:])    # "paso"

''' 
Comentario multi-línea:
Los strings en Python son inmutables, 
es decir, no se pueden modificar directamente.
Para cambiarlos, hay que crear nuevas cadenas
usando métodos o concatenación.
'''
