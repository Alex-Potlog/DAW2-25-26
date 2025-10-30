import sqlite3 as sql
import sys

def mostraMarques(nom):
    conexion = sql.connect('exemple.db')
    cursor = conexion.cursor()
    cursor.execute(f"SELECT nom, edat FROM usuaris WHERE nom = '{nom}';")
    resultats = cursor.fetchall()
    for i in resultats:
        print(i)

def ajuda():
    print('''Aquest script et permet accedir a la base de dades i consultar les 
seves dades''')

if __name__ == "__main__":
    try:
        match sys.argv[1]:
            case "-a" | "--atleta":
                mostraMarques(sys.argv[2])
            case "-h" | "--help":
                ajuda()
            case _:
                print("Fes servir els arguments correctes, buscals amb -h o --help")
    except Exception as e:
        print(e)
