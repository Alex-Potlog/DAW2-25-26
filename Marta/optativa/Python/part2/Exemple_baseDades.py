# sudo apt install sqlitebrowser
import sqlite3

# Crear o connectar-se a la base de dades
conn = sqlite3.connect('exemple.db')

# Crear un cursor per executar comandes SQL
cursor = conn.cursor()

# Crear una taula
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuaris (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    edat INTEGER
)
''')

# Inserir dades
cursor.execute('''
INSERT INTO usuaris (nom, edat)
VALUES (?, ?)
''', ("Anna", 25))

# Guardar els canvis
conn.commit()

# Llegir dades
cursor.execute('SELECT * FROM usuaris')
usuaris = cursor.fetchall()
for usuari in usuaris:
    print(usuari)

# Tancar la connexió
conn.close()