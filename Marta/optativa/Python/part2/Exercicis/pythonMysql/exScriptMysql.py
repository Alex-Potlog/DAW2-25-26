import sqlite3

# Crear o connectar-se a la base de dades
conn = sqlite3.connect('exemple.db')

# Crear un cursor per executar comandes SQL
cursor = conn.cursor()

"""1- Crea un script que donat un atleta ens mostri les seves marques:
Ha d'admetre les següents opcions:
-a o --atleta amb el nom de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes."""
# Crear una taula
cursor.execute('''
CREATE TABLE IF NOT EXISTS atletes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    edat INTEGER,
    llicencia TEXT,
    email TEXT,
    telefon VARCHAR(9)
)
''')

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS marques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    atleta_id INTEGER NOT NULL,           
    prova TEXT,
    resultat TEXT,
    data DATE,
    FOREIGN KEY (atleta_id) REFERENCES atletes(id)
)
''')

# Inserir dades
cursor.execute('''
INSERT INTO atletes (nom, edat, llicencia, email, telefon)
VALUES (?, ?, ?, ?, ?)
''', ("Anna", 25, "162738", "anna@gmail.com", "654782310"))

cursor.execute('''
INSERT INTO marques (atleta_id, prova, resultat, data)
VALUES (?, ?, ?, ?)
''', (1, "100m", "11.5s", "2025-03-15"))

# Guardar els canvis
conn.commit()

# Llegir dades
cursor.execute('SELECT * FROM atletes')
usuaris = cursor.fetchall()
for usuari in usuaris:
    print(usuari)

"""2- Crea un script que inserti un nou atleta a la base de dades.
Ha d'admetre les següents opcions:
-n amb el num. llicencia
-a amb el nom de l'atleta
-e amb l'email de l'atleta
-t amb el telèfon de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes."""
# Inserir dades
cursor.execute('''
INSERT INTO atletes (nom, edat, llicencia, email, telefon)
VALUES (?, ?, ?, ?, ?)
''', ("Mario", 28, "109283", "mario2@gmail.com", "668126403"))

cursor.execute('''
INSERT INTO marques (atleta_id, prova, resultat, data)
VALUES (?, ?, ?, ?)
''', (3, "200m", "20.19s", "2025-03-16"))

# Guardar els canvis
conn.commit()

# Llegir dades
cursor.execute('SELECT * FROM atletes')
usuaris = cursor.fetchall()
for usuari in usuaris:
    print(usuari)
    
# 3- Demana per teclat el nom d'una ciutat i executa la sentència "SELECT * FROM reunio WHERE lloc=%s". Mostra la quantitat de files obtingudes.

# 4- Modifica l'exercici 3, en cas de obtenir una quantitat de files > 0 mostra totes les dades amb un bucle.











# Tancar la connexió
conn.close()