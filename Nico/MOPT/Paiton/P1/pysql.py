#sudo dnf install sqlitebrowser
import sqlite3

conn = sqlite3.connect('exemple.db')

cursor = conn.cursor()

#Executa accions
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuaris (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    edat INTEGER
)
''')

cursor.execute('''
INSERT INTO USUARIS (nom, edat)
VALUES (?,?)
''',("Anna",25))

#Guarda els canvis
conn.commit()

#llegir dades
cursor.execute('SELECT * FROM usuaris')
usuaris = cursor.fetchall()
for usuari in usuaris:
    print(usuari)