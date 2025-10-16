#1-Demana per teclat una quantitat i a continuació entra per teclat diversos noms fins a la quantitat entrada. Al final mostra tots els noms per pantalla.
quant = int(input("Introdueix una quantitat: "))
noms = []
for i in range(quant):
    nom = input("Introdueix un nom: ")
    noms.append(nom)
print("Els noms introduits son:")
for nom in noms:
    print(f"{nom}")
    
#2-Igual a l’exercici 1, però sense permetre noms repetits.
quant = int(input("Introdueix una quantitat: "))
noms = []
for i in range(quant):
    nom = input("Introdueix un nom: ")
    if nom not in noms:
        noms.append(nom)
    else:
        print("El nom ja existeix, introdueix un altre nom.")
print("Els noms introduits son:")
for nom in noms:
    print(f"{nom}")
#3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:
#{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

#Demana les dades per teclat i mostra la informació al final. Si l’individu és major d’edat, afegeix “(major d’edat)”.
vnom = input("Entra nom:")
vcog = input("Entra cognom:")
vedat = int(input("Entra edat:"))
vpes = float(input("Entra pes:"))
individu = {"nom" : vnom , "cognom":vcog ,"edat":vedat ,"Pes":vpes}
print(f"El individu es diu {individu['nom']} {individu['cognom']}, te {individu['edat']} anys i pesa {individu['Pes']} Kg")
if vedat >= 18:
    print("(Major d'edat)")


#4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
individus = [
    {"nom": "Anna", "cognom": "Garcia", "edat": 22, "pes": 60.5},
    {"nom": "Pere", "cognom": "Lopez", "edat": 17, "pes": 70.0},
    {"nom": "Maria", "cognom": "Martinez", "edat": 30, "pes": 55.0},
    {"nom": "Joan", "cognom": "Sanchez", "edat": 16, "pes": 68.0},
    {"nom": "Laura", "cognom": "Hernandez", "edat": 25, "pes": 62.0},
    #{"nom": "Laura", "cognom": "Hernandez", "edat": 25, "pes": 62.0},
    #{"nom": "Laura", "cognom": "Hernandez", "edat": 25, "pes": 62.0}
]

#Mostra el contingut de tota la llista segons s’indica a l’exercici 3.
for individu in individus:
    print(f"El individu es diu {individu['nom']} {individu['cognom']}, te {individu['edat']} anys i pesa {individu['pes']} Kg")
    if individu['edat'] >= 18:
        print("(Major d'edat)")


#Mostra la quantitat d’individus majors d’edat.
majors_edat = sum(1 for individu in individus if individu['edat'] >= 18)
print(f"Quantitat d'individus majors d'edat: {majors_edat}")


#Mostra la mitjana del pes de tots els individus.
mitjana_pes = sum(individu['pes'] for individu in individus) / len(individus)
print(f"Mitjana del pes de tots els individus: {mitjana_pes:.2f} Kg")

#Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.
noms_vistos = set()
noms_repetits = set()
for individu in individus:
    nom = individu['nom']
    if nom in noms_vistos:
        noms_repetits.add(nom)
    else:
        noms_vistos.add(nom)
if noms_repetits:
    print(f"Noms repetits: {noms_repetits}")
else:
    print("SENSE NOMS REPETITS")
