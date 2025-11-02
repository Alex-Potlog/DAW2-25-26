import sqlite3 


# conn = sqlite3.connect("exemple.db")

# cursor =conn.cursor()

# try:
#     cursor.execute("""create table articulos (
#                             codigo integer primary key autoincrement,
#                             descripcion text,
#                             precio float
#                         )""")
#     print("se creo la tabla articulos")                        
# except sqlite3.OperationalError:
#     print("La tabla articulos ya existe")    

# cursor.execute('''
# INSERT INTO articulos (descripcion, precio)
# VALUES (?, ?)
# ''', ("Si", 25))

# # Guardar els canvis
# conn.commit()

# # Llegir dades
# cursor.execute('SELECT * FROM articulos')
# usuaris = cursor.fetchall()
# for usuari in usuaris:
#     print(usuari)

# # Tancar la connexió
# conn.close()


"""1- Crea un script que donat un atleta ens mostri les seves marques:
Ha d'admetre les següents opcions:
-a o --atleta amb el nom de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne 
un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes."""


# conn = sqlite3.connect("exemple.db")

# cursor=conn.cursor()
# text=""

# while "-a" not in text:
#     text=input("introdueix l'atleta")
#     if "-h" in text or "--help" in text:
#         print("Funciona posant -a al final")

# cursor.execute(''' select * from articulos where descripcio ==?''',(text,))

# resultats = cursor.fetchall()

# if resultats:
#     for fila in resultats:
#         print(fila)
# else:
#     print("No s'han trobat resultats")

# conn.close()


# """2- Crea un script que inserti un nou atleta a la base de dades.
# Ha d'admetre les següents opcions:
# -n amb el num. llicencia
# -a amb el nom de l'atleta
# -e amb l'email de l'atleta
# -t amb el telèfon de l'atleta
# --help o -h mostra un missatge informatiu del funcionament.
# Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. 
# Si hi ha diverses opcions, les ha de gestionar totes."""

# descripcion =str(input("insereix la descripcio"))
# preu=int(input("Introdueix el preu")) 

# conn = sqlite3.connect("exemple.db")

# cursor=conn.cursor()

# try:
#     cursor.execute(''' insert into articulos(descripcion,precio) values (?,?)''',(descripcion,preu))
# except sqlite3.OperationalError as e:
#     raise 

# conn.commit()

# conn.close()

# """3- Demana per teclat el nom d'una ciutat i executa la sentència 
# "SELECT * FROM reunio WHERE lloc=%s". Mostra la quantitat de files obtingudes."""

desc = str(input("Intodueix la ciutat"))

conn =sqlite3.connect("exemple.db")

cursor = conn.cursor()

try:
    cursor.execute(''' select * from articulos where descripcion=?''',(desc,))
except FileNotFoundError as e:
    raise FileNotFoundError(e)

results= cursor.fetchall()

for element in results:
    print(element)

conn.close()