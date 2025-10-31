import sqlite3
import argparse
#import sys

#S'ha de crear un parser
parser=argparse.ArgumentParser(#Creem el gestor d'arguments
    description='Script per consultar marques d\'atletes'
)

#Afegir les opcions que ens demana a l'enunciat
parser.add_argument(#defini les opcions que podrem fer servir
    '-a', '--atleta',
    type=str,
    help='Nom de l\'atleta a consultar'
)

parser.add_argument(
    '-n', '--llicencia',
    type=str,
    help= 'Número de llicència a consultar'
)

parser.add_argument(
    '-e', '--email',
    type=str,
    help='email de l\'atleta a consultar' 
)

parser.add_argument(
    '-t', '--telefon',
    type=str,
    help='el telèfon de l\'atleta a consultar'
)

#Parsejar arguments
arg=parser.parse_args() #Processament dels arguments que l'usuari a introduit

# Fem servir els aguments
# Connectar a la BD
conn = sqlite3.connect('exemple.db')
cursor = conn.cursor()

try:
    if arg.atleta: #té el valor que l'usuari ha posat després de -a
        nom_atleta = arg.atleta
        print(f"Buscant atleta: {nom_atleta}")
        
        # Aquí faràs la consulta a la BD
        # Buscar l'atleta i les seves marques
        cursor.execute('''
            SELECT a.nom, m.prova, m.resultat, m.data
            FROM atletes a
            JOIN marques m ON a.id = m.atleta_id
            WHERE a.nom = ?
        ''', (nom_atleta,))

        marques = cursor.fetchall()

            # Mostrar resultats
        if marques:
            print(f"\nMarques de {nom_atleta}:")
            for marca in marques:
                print(f"  - {marca[1]}: {marca[2]} ({marca[3]})")
        else:
            print(f"No s'han trobat marques per a {nom_atleta}")

    elif arg.llicencia: # Cerca per llicència
        num_llicencia=arg.llicencia
        print(f"Buscant l'atleta amb llicència; {num_llicencia} ")

        # Buscar l'atleta i les seves marques
        cursor.execute('''
            SELECT a.nom, m.prova, m.resultat, m.data
            FROM atletes a
            JOIN marques m ON a.id = m.atleta_id
            WHERE a.llicencia = ?
        ''', (num_llicencia,))

        marques = cursor.fetchall()

            # Mostrar resultats
        if marques:
            print(f"\nMarques de {num_llicencia}:")
            for marca in marques:
                print(f"  - {marca[1]}: {marca[2]} ({marca[3]})")
        else:
            print(f"No s'han trobat marques per a {num_llicencia}")
        
    elif arg.email:
        email_atleta=arg.email
        print(f"Buscant l'atleta amb llicència; {email_atleta} ")

        # Buscar l'atleta i les seves marques
        cursor.execute('''
            SELECT a.nom, m.prova, m.resultat, m.data
            FROM atletes a
            JOIN marques m ON a.id = m.atleta_id
            WHERE a.email = ?
        ''', (email_atleta,))

        marques = cursor.fetchall()

            # Mostrar resultats
        if marques:
            print(f"\nMarques de {email_atleta}:")
            for marca in marques:
                print(f"  - {marca[1]}: {marca[2]} ({marca[3]})")
        else:
            print(f"No s'han trobat marques per a {email_atleta}")

    elif arg.telefon:
        num_telf=arg.telefon
        print(f"Buscant l'atleta amb llicència; {num_telf} ")

        # Buscar l'atleta i les seves marques
        cursor.execute('''
            SELECT a.nom, m.prova, m.resultat, m.data
            FROM atletes a
            JOIN marques m ON a.id = m.atleta_id
            WHERE a.telefon = ?
        ''', (num_telf,))

        marques = cursor.fetchall()

            # Mostrar resultats
        if marques:
            print(f"\nMarques de {num_telf}:")
            for marca in marques:
                print(f"  - {marca[1]}: {marca[2]} ({marca[3]})")
        else:
            print(f"No s'han trobat marques per a {num_telf}")
    else:
        print("Error: Has de proporcionar un nom d'atleta amb -a o --atleta")
        parser.print_help() #Per tenir una millor gestió d'errors
finally:
    conn.close()