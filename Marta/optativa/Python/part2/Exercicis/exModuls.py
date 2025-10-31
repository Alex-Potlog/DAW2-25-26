'''1- Crea un script per realitzar còpia de seguretat de diversos orígens.

Farà falta una funció per a fer la còpia d'un origen a un destí.

def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.

L'script tindrà una variable amb la llista d'orígens que s'han de copiar i una altra variable amb el destí de les còpies.

origens=['/home/usuari/', '/root/', '/etc/', '/dades/']  # Fan falta drets de lectura

desti='/copies/'  # Fan falta drets d'escriptura

S'ha de fer un bucle per recorrer la llista origens i fer la còpia de cada un.

Funcions útils:
os.path.join(path, path2, ...)  EX:  nom=os.path.join("/info/",  desti)
shutil.copytree(src, dst,  dirs_exist_ok=True)
shutil.copy2(src, dst)
os.makedirs(os.path.dirname(desti), exist_ok=True)
os.path.isdir(path)
'''






'''2- Crea un script per realitzar la restauració de la còpia de seguretat anterior.

L'script tindrà dues variables: origen de les còpies i destí de restauració.

copies='/copies/'  # Fan falta drets de lectura

desti='/proves/'  # Fan falta drets d'escriptura

Funcions útils:

os.listdir(path)  Ex:  llista=os.listdir('/copies')'''







'''3- Modifica els scripts per permetre tenir diverses còpies. Es tracta d'afegir una variable amb la quantitat de còpies a conservar. S'hauran de crear diversos directoris amb les còpies.
S'han de conservar la quantitat de còpies indicades, sempre les últimes n còpies fetes. En fer la restauració farà falta saber quina és la còpia que volem restaurar.
Exemple:
desti='/home/dades/copies/'
ncopies=5

Això crearia:

/home
  |
  --dades
     |
     --copies
        |
        --1
        |
        --2
        |
        --3
        |
        --4
        |
        --5
 

Si ja hem completat totes les possibles còpies i en volem fer una més, s'haurà de sobreescriure la més antiga.

Funcions útils:
os.path.getmtime(path)
os.path.isdir(path)'''






""" 4- Unifica els scripts i selecciona la tasca a realitzar segons els paràmetres que rebi.
Nom script: filesadm.py

Paràmetres:
-h --help                   Missatge informatiu del funcionament.
-b --backup              Fa la còpia de seguretat.
-r --restore               Recupera l'última còpia guardada.
-R num --restn num Recupera la còpia amb número num.
-d path --dest path   Destí de les còpies de seguretat.
-n num                     Quantitat de còpies de seguretat guardades.
-o --overwrite           Permet sobreescriure les dades guardades o recuperades.
5- Crea un script que accepti els següents paràmetres:
-m --missatge          Mostra el text "Missatge de prova"
-f text --frase text     Mostra "FRASE: " i el text passat per paràmetre
-h --help                   Mostra informació sobre com fer servir aquest script """




# 6- Crea un script que mostri el contingut d'un directori passat per paràmetre.





# 7- Crea un script que faci la creació d'un directori amb el nom passat per paràmetre.






# 8- Crea un script que mostri la data de creació d'un fitxer o directori passat per paràmetre.