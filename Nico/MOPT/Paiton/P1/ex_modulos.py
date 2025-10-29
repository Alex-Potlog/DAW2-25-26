'''
1- Crea un script per realitzar còpia de seguretat de diversos orígens.

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
os.path.isdir(path)'''
import os
import shutil

def copia_dades(origen, desti):
    nom_copia = os.path.basename(os.path.normpath(origen))
    desti_final = os.path.join(desti, nom_copia)
    if os.path.isdir(origen):
        shutil.copytree(origen, desti_final, dirs_exist_ok=True)
    else:
        os.makedirs(os.path.dirname(desti_final), exist_ok=True)
        shutil.copy2(origen, desti_final)

origens=['/home/usuari/', '/root/', '/etc/', '/dades/']  # Fan falta drets de lectura

desti='/copies/'  # Fan falta drets d'escriptura

for origen in origens:
    copia_dades(origen, desti)

'''2- Crea un script per realitzar la restauració de la còpia de seguretat anterior.

L'script tindrà dues variables: origen de les còpies i destí de restauració.

copies='/copies/'  # Fan falta drets de lectura

desti='/proves/'  # Fan falta drets d'escriptura

Funcions útils:

os.listdir(path)  Ex:  llista=os.listdir('/copies')'''

copies='/copies/'  # Fan falta drets de lectura

desti='/proves/'  # Fan falta drets d'escriptura

def restaura_dades(origen, desti):
    llista = os.listdir(origen)
    for item in llista:
        origen_item = os.path.join(origen, item)
        desti_item = os.path.join(desti, item)
        if os.path.isdir(origen_item):
            shutil.copytree(origen_item, desti_item, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(desti_item), exist_ok=True)
            shutil.copy2(origen_item, desti_item)

restaura_dades(copies, desti)

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
import sys

def multiple_copies(origens, desti_base, ncopies):
    desti_dirs = [os.path.join(desti_base, str(i)) for i in range(1, ncopies + 1)]
    
    # Check existing copies and sort by modification time
    existing_copies = [d for d in desti_dirs if os.path.isdir(d)]
    existing_copies.sort(key=os.path.getmtime)
    
    # If we have reached the maximum number of copies, remove the oldest
    if len(existing_copies) >= ncopies:
        shutil.rmtree(existing_copies[0])
        existing_copies.pop(0)
    
    # Shift existing copies
    for i in range(len(existing_copies), 0, -1):
        new_desti = os.path.join(desti_base, str(i + 1))
        shutil.move(existing_copies[i - 1], new_desti)
    
    # Create new copy in the first directory
    new_desti = os.path.join(desti_base, '1')
    os.makedirs(new_desti, exist_ok=True)
    
    for origen in origens:
        copia_dades(origen, new_desti)
