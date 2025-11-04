import sqlite3 as sql
import sys

def inserta_atleta(num, nom, email, telefon):
    if None in (num, nom, email, telefon):
        raise ValueError("Tots els paràmetres són obligatoris.")
    conn = sql.connect('atletes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS atletes (
            num INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            email TEXT NOT NULL,
            telefon TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO atletes (num, nom, email, telefon)
        VALUES (?, ?, ?, ?)
    ''', (num, nom, email, telefon))
    conn.commit()
    cursor.execute('SELECT * FROM atletes')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print(f"Atleta {nom} inserit correctament a la base de dades.")

def show_help():
    print("Per insertar un atleta, proporciona els següents detalls:")
    print("Num: -n")
    print("Nom: -a")
    print("Email: -e")
    print("Telèfon: -t")

if __name__ == "__main__":
    try:
        llista_args = {
            '-n': None,
            '-a': None,
            '-e': None,
            '-t': None
        }

        if len(sys.argv) != 9:
            show_help()
            sys.exit(0)

        for i in range(1, len(sys.argv)):
            if sys.argv[i] in llista_args:
                llista_args[sys.argv[i]] = sys.argv[i + 1]

        inserta_atleta(
            llista_args['-n'],
            llista_args['-a'],
            llista_args['-e'],
            llista_args['-t']
        )

    except Exception as e:
        print(f"Error: {e}")