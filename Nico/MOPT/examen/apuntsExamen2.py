#1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

def mostra(nomfitxer):
    try:
        fitxer=open(nomfitxer, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer)
        return
    for linia in fitxer:
        print(linia, end='')
    fitxer.close()

#2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.

def concatena(nomfitxer1, nomfitxer2):
    try:
        fitxer2=open(nomfitxer2, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer2)
        return
    try:
        fitxer1=open(nomfitxer1, "a")
    except FileNotFoundError:
        print("No pot crear-se", nomfitxer1)
        return
    for linia in fitxer2:
        fitxer1.write(linia)
    fitxer1.close()
    fitxer2.close()
    return

#3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.

def afegir(llista, nomfitxer):
    try:
        fitxer=open(nomfitxer, "a")
    except FileNotFoundError:
        print("No pot crear-se", nomfitxer)
        return
    for e in llista:
        fitxer.write(e+"\n")
    fitxer.close()
    return

#4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.

import sys, os
def escriuPos(frase, pos, nomfitxer):
    try:
        fitxer=open(nomfitxer, "r+")
    except FileNotFoundError:
        try:
            fitxer=open(nomfitxer, "w+")
        except FileNotFoundError:
            print("No pot crear-se", nomfitxer)
            return
    if pos < 0:
        print("Posició incorrecta")
        return
    mida=fitxer.seek(0, os.SEEK_END)
    if pos>mida:
        fitxer.write(' '*(pos-mida))  # opcional omplir amb espais
    fitxer.seek(pos)
    fitxer.write(frase)
    fitxer.close()
    return
'''
1- Crea un script que busqui una paraula dins d'un fitxer de text. Ha de mostrar la quantitat de vegades que ha trobat la paraula.
Ha d'admetre les següents opcions:
-f o --fitxer amb el nom del fitxer.
-p o --paraula amb la paraula que volem trobar.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.
'''
import getopt, sys

def quantesParaules(nomfitxer, paraula):
    if not nomfitxer or not paraula: return 0
    try:
        fitxer=open(nomfitxer, "r")
    except FileNotFoundError:
        return 0
    compt=0
    for linia in fitxer:
        compt = compt + linia.count(paraula)
    fitxer.close()
    return compt
    
def usage():
    print("Mostra la quantitat de vegades que ha trobat una paraula dins d'un fitxer de text.\n"+
            "Opcions vàlides:\n"+
            "-f o --fitxer amb el nom del fitxer.\n"+
            "-p o --paraula amb la paraula que volem trobar.\n"+
            "--help o -h mostra un missatge informatiu del funcionament.\n")
   
def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "f:p:h",
            ["fitxer=", "paraula=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
        
    if not opts:
        usage()
    
    paraula=None
    fitxer=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--fitxer"):
            fitxer=a
        elif o in ("-p", "--paraula",):
            paraula=a
        else:
            print("Opció desconeguda")
    
    if fitxer and paraula:
        print("La paraula",paraula, "surt", quantesParaules(fitxer, paraula))
        
if __name__=="__main__":
    main()


'''
2- Crea un script que insereixi una frase en un número de fila d'un fitxer de text. No ha de sobreescriure, ha de inserir a la fila indicada i conservar la resta de dades del fitxer.
Ha d'admetre les següents opcions:
-f o --fitxer amb el nom del fitxer.
-t o --text amb la frase que volem inserir.
-p o --pos amb el número de fila a on fer l'insert.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.
Exemple:
Si posició=0 i text="Con diez cañones por banda,"
Fitxer original:
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;
Fitxer final:
Con diez cañones por banda,
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;
'''
import getopt, sys, shutil

def usage():
    print("Opcions vàlides:\n"+
          "-f o --fitxer  nom del fitxer.\n"+
          "-t o --text    frase que volem inserir.\n"+
          "-p o --pos     posició a on fer l'insert.\n"+
          "--help o -h    mostra un missatge informatiu del funcionament.\n")

def inserta(nomfitxer, frase, pos):
    if not nomfitxer or not frase:
        return
    if pos is None or pos < 0:
        return
    try:
        fitxer=open(nomfitxer, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer)
        return
    try:
        fitxer_tmp=open("file_temp.txt", "w")
    except FileNotFoundError:
        print("No pot crear-se file_temp.txt")
        return
    except PermissionError:
        print("No pot crear-se file_temp.txt")
        return
    num_linia=0
    for linia in fitxer:
        if num_linia==pos:
            #escriu la frase a la pos indicada
            fitxer_tmp.write(frase+"\n")
            num_linia=num_linia+1
        fitxer_tmp.write(linia)
        num_linia=num_linia+1
    #La línia es posterior al final del fitxer
    if pos>=num_linia:
        for n in range(pos-num_linia):
            fitxer_tmp.write("\n")
        fitxer_tmp.write(frase+"\n")
        
    fitxer.close()
    fitxer_tmp.close()
    #rename del fitxer temporal
    shutil.move("file_temp.txt", nomfitxer)
    return
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:t:p:h", ["fitxer=", "text=", "pos=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
        
    if not opts:
        usage()
    
    nfitxer=None
    frase=None
    pos=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--fitxer"):
            nfitxer=a
        elif o in ("-t", "--text"):
            frase=a
        elif o in ("-p", "--pos"):
            try:
                pos=int(a)
                if pos<0:
                    print("Posició incorrecta")
                    pos=None
            except:
                print("Posició incorrecta")
                pos=None
        else:
            print("Opció desconeguda")
    
    inserta(nfitxer, frase, pos)
    
if __name__=="__main__":
    main()



'''
3- Programa un script que creï un nou fitxer de text amb contingut de part d'un altre fitxer.
Ha d'admetre les següents opcions:
-o o --origen amb el nom del fitxer origen.
-d o --desti amb el nom del fitxer nou.
--liniai amb la primera línia que volem guardar, comptant des d'1.
--liniaf amb l'última línia que volem guardar, comptant des d'1.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.
Exemple:
Si liniai=2 i liniaf=3
Fitxer origen:
Con diez cañones por banda,
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;
Fitxer nou:
viento en popa a toda vela,
no corta el mar, sino vuela
'''
import getopt, sys

def usage():
    print("Opcions vàlides:\n"+
          "Crea un nou fitxer de text amb contingut de part d'un altre fitxer.\n"+
          "-o o --origen amb el nom del fitxer origen.\n"+
          "-d o --desti amb el nom del fitxer nou.\n"+
          "--liniai amb la primera línia que volem guardar, comptant des d'1.\n"+
          "--liniaf amb l'última línia que volem guardar, comptant des d'1.\n"+
          "--help o -h mostra un missatge informatiu del funcionament.\n")

def fragment(nomorigen, nomdesti, liniai, liniaf):
    if not nomorigen or not nomdesti:
        return
    try:
        fitxer=open(nomorigen, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomorigen)
        return
    try:
        fitxer_dst=open(nomdesti, "w")
    except FileNotFoundError:
        print("No pot crear-se", nomdesti)
        return
    except PermissionError:
        print("No pot crear-se", nomdesti)
        return
    num_linia=1
    for linia in fitxer:
        if num_linia>=liniai and num_linia<=liniaf:
            fitxer_dst.write(linia)
        num_linia=num_linia+1
    fitxer.close()
    fitxer_dst.close()
    return
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:d:h", ["origen=", "desti=", "liniai=", "liniaf=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
        
    if not opts:
        usage()
    
    nomorigen=None
    nomdesti=None
    liniai=None
    liniaf=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-o", "--origen"):
            nomorigen=a
        elif o in ("-d", "--desti"):
            nomdesti=a
        elif o == "--liniai":
            liniai=int(a)
        elif o == "--liniaf":
            liniaf=int(a)
        else:
            print("Opció desconeguda")
    
    fragment(nomorigen, nomdesti, liniai, liniaf)
    
if __name__=="__main__":
    main()
    '''
1- Crea un script que donat un atleta ens mostri les seves marques:
Ha d'admetre les següents opcions:
-a o --atleta amb el nom de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
'''
import mysql.connector  # pip install mysql-connector-python
import getopt, sys

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def mostraMarques(db, atleta):
    cursor = db.cursor()
    cursor.execute("SELECT descripcio, datamarca, registre FROM marca NATURAL JOIN atleta \
                            NATURAL JOIN especialitat WHERE nomatleta=%s", (atleta,))
    result = cursor.fetchall()
    if not result:
        print("No hi ha marques d'aquest atleta")
    else:
        for descr, data, regis in result:
            print(descr, data, regis)
    cursor.close()

def usage():
    print("Mostra un atleta i les seves marques.\n"+
            "Opcions vàlides:\n"+
            "-a o --atleta amb el nom de l'atleta.\n"+
            "-h o --help   mostra un missatge informatiu del funcionament.\n")
   
def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "a:h",
            ["atleta=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
        
    if not opts:
        usage()

    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    atleta=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-a", "--atleta"):
            atleta=a
        else:
            print("Opció desconeguda")
    
    if atleta:
        mostraMarques(db, atleta)
    db.close()
        
if __name__=="__main__":
    main()



'''
2- Crea un script que inserti un nou atleta a la base de dades.
Ha d'admetre les següents opcions:
-n amb el num. llicencia
-a amb el nom de l'atleta
-e amb l'email de l'atleta
-t amb el telèfon de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
'''
import mysql.connector  # pip install mysql-connector-python
import getopt, sys

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def insertaAtleta(db, nllicencia, nomatleta, email, telefon):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO atleta \
            VALUES (%s, %s, %s, %s)",
            (nllicencia, nomatleta, email, telefon))
        db.commit()
    except Exception as err:
        print("No es pot l'insert:", err)
    cursor.close()

def usage():
    print("Inserta un nou atleta a la base de dades.\n"+
        "-n  núm. llicencia\n"+
        "-a  nom de l'atleta\n"+
        "-e  email de l'atleta\n"+
        "-t  telèfon de l'atleta\n"+
        "--help o -h mostra aquest missatge.\n")
   
def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "n:a:e:t:h",
            ["help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
        
    if not opts:
        usage()

    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    num=atleta=email=telef=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o=="-n":
            num=a
        elif o=="-a":
            atleta=a
        elif o=="-e":
            email=a
        elif o=="-t":
            telef=a
        else:
            print("Opció desconeguda")
    
    if num and atleta and email and telef:
        insertaAtleta(db, num, atleta, email, telef)
    else:
        print("Falten dades per a fer l'insert")
    
    db.close()
        
if __name__=="__main__":
    main()



#3- Demana per teclat el nom d'una ciutat i executa la sentència "SELECT * FROM reunio WHERE lloc=%s". Mostra la quantitat de files obtingudes.

import mysql.connector  # pip install mysql-connector-python

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def getFiles(db, ciutat):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reunio WHERE lloc=%s", (ciutat, ))
    cursor.fetchall()
    files=cursor.rowcount
    cursor.close()
    return files

def main():
    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
    
    ciutat=input("Entra un nom de ciutat:")
    
    print("La quantitat de reunions és", getFiles(db, ciutat))

    db.close()
        
if __name__=="__main__":
    main()



#4- Modifica l'exercici 3, en cas de obtenir una quantitat de files > 0 mostra totes les dades amb un bucle.

import mysql.connector  # pip install mysql-connector-python

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def getFiles(db, ciutat):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reunio WHERE lloc=%s", (ciutat, ))
    for cod, nom, ciutat, diai, diaf in cursor.fetchall():
        print(cod, nom, ciutat, diai, diaf)
    files=cursor.rowcount
    cursor.close()
    return files

def main():
    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
    
    ciutat=input("Entra un nom de ciutat:")
    
    print("La quantitat de reunions és", getFiles(db, ciutat))

    db.close()
        
if __name__=="__main__":
    main()