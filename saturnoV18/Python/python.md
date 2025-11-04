# Metodos de manipulacion de cadenas
Los metodos mas importantes son los siguientes.
- .upper()              #Transforma la cadena a mayusculas
- .lower()              #Transforma la cadena a minusculas
- .capitalize()         #Pone la primera letra de cada palabra en mayusculas
- .isalnum()            #Mira si la cadena esta compuesta por numeros y caracteres a, b, c...
- .isnumeric()          #Mira si la cadena esta compuesta de numeros
- .isalpha()            #Mira si la cadena esta compuesta de caracteres a, b, c...
- .isupper()            #Mira si la cadena esta en mayusculas
- .islower()            #Mira si la cadena esta en minusculas
- .replace("a", "A")    #Reemplaza el contenido

# Array o lista
Es una lista que puede tener diferentes valores y de diferentes tipos.
lista = []

Se puede acceder al contenido del array de diversas formas.
- lista[0]  #Accede al primer elemento de la lista
- lista[-1] #Accede al ultimo elemento de la lista

Los metodos mas importantes para las listas son los siguientes.
- .append(el)       #Añade al final de la lista
- .insert(pos, el)  #Inserta el elemento en una posicion determinada
- .remove(el)       #Quita un elemento determinado de la lista
- .pop()            #Quita el ultimo elemento de la lista, si se le pasa un indice el que este en esa posicion
- .sort()           #Ordena la lista
- .reverse()        #Invierte las posiciones de la lista
- random.shuffle(l) #Mezcla la lista (hay q hacer import random)
- sum(lista)        #Suma todos los elementos de la lista
- max(lista)        #Devuelve el numero mas grande de la lista
- min(lista)        #Devuelve el numero mas pequeño de la lista

# Operaciones basicas de listas-cadenas
- a + b             #Une dos listas-cadenas
- b = a[ini:]       #Crea una subcadena-sublista de a desde la posicion indicada en el ini
- b = a[:fin]       #Crea una subcadena-sublista de a desde el inicio hasta la posicion de fin, sin incluir esta
- b = a[ini:fin]    #Crea una subcadena-sublista de a desde la posicion indicada en el ini hasta la posicion de fin, sin incluir esta
- len(a)            #Muestra la longitud de la lista-cadena
- a in b            #Mira si a esta dentro de b, si queremos mirar que no este hay que poner un not delante de in
- cadena.find("a")  #Busca la posicion de un str dentro de cadena
- lista.indexof(2)  #Busca la posicion de 2 dentro de lista
- a.count("patata") #Cuenta las veces que aparece la palabra patata en una cadena o lista

# __name__
__name__ es una variable especial que Python asigna automáticamente.
Si el archivo se está ejecutando directamente (por ejemplo, python mi_programa.py), entonces __name__ toma el valor "__main__".
Si el archivo se importa desde otro archivo, entonces __name__ toma el nombre del módulo (por ejemplo, "mi_programa").
Para hacer el main de otros lenguajes de programacion hay que hacer lo siguiente:

if __name__ == "__main__":
    main() #ejecutar la funcion main
    
# getopt
Sirve para pasar los parametros del programa, su estructura es la siguiente:
opts, args = getopt.getopt(
    sys.argv[1:],       #Texto del comando excluyendo el nombre del fichero
    "a:h",              #Parametros cortos (-h)
    ["atleta=", "help"] #Parametros largos (--help) (para atleta como que lleva un = habra que pasarle tambien un valor, ej: --atleta=Mesi)
)

Una manera de recorrerlo seria la siguiente:

import sys, getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "a:h", ["atleta=", "help"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)
for opt, val in opts:
    if opt in ("-h", "--help"):
        print("Uso: script.py -a <nombre_atleta>")
    elif opt in ("-a", "--atleta"):
        print("Atleta recibido:", val)

# sys.exit()
Sale del programa con un codigo, por defecto devuelve 0,
Los mas comunes son los siguientes
- sys.exit()        #Devuelve 0
- sys.exit(1)       #Devuelve 1 (Error generico)
- sys.exit(2)       #Devuelve 2 (Uso incorrecto del comando o argumentos)
- sys.exit("text")  #Devuelve 1 y un texto explicativo del error

# Lectura de ficheros
Para leer un fichero primero tenemos que abrirlo, esto se hace de la siguiente manera.
f = open("nombreFichero")
Tambien se le pueden pasar opciones como segundo parametro, las opciones mas habituales son las siguientes.
- r     #Opcion por defecto, permite la lectura de datos.
- w     #Crea un fichero y permite escribir en el. Si ya existe este fichero lo sobreescribe.
- a     #Añade al final del fichero.
- x     #Crea un fichero, si existe da error.
- b     #Sirve para leer un fichero binario.

Para leer el fichero hay que utilizar la funcion read de las siguientes maneras.
- f.read()      #Lee todo el fichero.
- f.readline()  #Lee una linea o el numero de lineas especificadas en la funcion.
- f.write()     #Escribe en el fichero un str que le especifiquemos a la funcion. Por defecto no hace salto de linea.
- f.close()     #Cierra el fichero.

# Funciones
Las funciones se crean con def y pueden devolver diversos parametros. Se le puedo poner en los parametros parametros="hola" para definir el valor por defecto si no se especifica.
def nombreDeLaFuncion(parametros):
    #contenido
    return valor1, valor2
    
valor1, valor2 = nombreDeLaFuncion(parametros)

Hay otro tipo de funciones que son las denominadas lambda que se crean de la siguiente manera.
cuadrado = lambda x: x * x
print(cuadrado(4))  # 16

# Bases de datos y persistencia
Para guardar los datos de manera permanente normalmente se utiliza una base de datos.
Para utilizar la base de datos sqlite3 hay que hacerlo de la siguiente manera.
import sqlite3
try:
    con = sqlite3.connect("nombreDelArchivoDeBaseDeDatos.db")   #Hace la conexion con la base de datos, si no existe la crea
    cursor = con.cursor()       #Crea un cursor que nos permite ejecutar comandos
    bd = "anime"                #Nombre de la tabla en la base de datos
    cursor.execute("SELECT * FROM ?", (bd))     #Ejecuta el comando sql, pone en el interrogante el valor que le pasemos por el segundo parametro dentro del parentesis
    datos = cursor.fetchall()   #Recoge el resultado de el execute y muestra solo el nombre del anime
    for id, anime, episodios in datos:
        print(anime)
except Exception as e:
    print(e)
    
Si modificamos algo en la base de datos y queremos que se guarde hay que hacer lo siguiente.
cursor.execute('DELETE FROM anime WHERE id = ?', (str(id)))
con.commit()

Algunas funciones de la base de datos son:
- Crear una tabla.
cursor.execute("""
CREATE TABLE IF NOT EXISTS atletas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    pais TEXT
)
""")
conexion.commit()  # Guarda los cambios en el archivo

- Insertar datos.
cursor.execute("INSERT INTO atletas (nombre, edad, pais) VALUES (?, ?, ?)", 
               ("Messi", 36, "Argentina"))
conexion.commit()

- Leer datos.
cursor.execute("SELECT * FROM atletas")
filas = cursor.fetchall()  # Trae todas las filas

for fila in filas:
    print(fila)

- Actualizar datos.
cursor.execute("UPDATE atletas SET edad = ? WHERE nombre = ?", (37, "Messi"))
conexion.commit()

- Eliminar datos.
cursor.execute("DELETE FROM atletas WHERE nombre = ?", ("Messi",))
conexion.commit()

- Cerrar la conexion
conexion.close()

