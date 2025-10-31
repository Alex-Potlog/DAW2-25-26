#1-Demana per teclat una quantitat i a continuació entra per teclat diversos 
# noms fins a la quantitat entrada. Al final mostra tots els noms per pantalla.
num1=int(input("Escriu un número: "))

nom=[]
i=0

while (i<num1):
    nom1=(input("Escriu un nom: "))
    nom.append(nom1)

    i+=1

nomm=" ".join(nom)

print(f"La llista de noms és: {nomm}".format())
print("------------------------------------------------------------------\n")
#2-Igual a l’exercici 1, però sense permetre noms repetits.
num2=int(input("Escriu un número: "))

nom2=[]
i=0

while (i<num2):
    nomB=(input("Escriu un nom: "))
    if nomB not in nom2:
        nom2.append(nomB)

    i+=1

nomm=" ".join(nom2)

print(f"La llista de noms és: {nomm}".format())
print("------------------------------------------------------------------\n")

#3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:
# {“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }
# Demana les dades per teclat i mostra la informació al final. Si l’individu és major d’edat, afegeix “(major d’edat)”.
individus=dict()

individus['nom']=(input("Escriu el nom: "))
individus['Cognom']=(input("Escriu el cognom: "))
individus['Edat']=int(input("Escriu l'edat: "))
individus['pes']=float(input("Escriu el pes: "))

if individus['Edat']>=18:
    nova_dada={'major': "(Major d'edat)"}
    individus.update(nova_dada)
    print(f"Aquestes són les dades: {individus['nom']} {individus['Cognom']} {individus['Edat']} {individus['pes']} {individus['major']}")
else:
    print(f"Aquestes són les dades: {individus['nom']} {individus['Cognom']} {individus['Edat']} {individus['pes']}")
print("------------------------------------------------------------------\n")
#4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
lista =[
    {'nom':"Marta", 'cognom':"Llabrés", 'edat':33, 'pes':70, 'major':"(Major edat)"},
    {'nom':"Eric", 'cognom':"Fernandez", 'edat':15, 'pes':54},
    {'nom':"Alicia", 'cognom':"Castro", 'edat':20, 'pes':62, 'major':"(Major edat)"},
    {'nom':"Pau", 'cognom':"Torrent", 'edat':26, 'pes':77, 'major':"(Major edat)"},
    {'nom':"Laura", 'cognom':"Perez", 'edat':12, 'pes':50},
]

for elem in lista:
    if elem['edat']>=18:
        print(f"Aquestes són les dades: {elem['nom']} {elem['cognom']} {elem['edat']} {elem['pes']} {elem['major']}")
    else:
        print(f"Aquestes són les dades: {elem['nom']} {elem['cognom']} {elem['edat']} {elem['pes']} ")
print("------------------------------------------------------------------\n")
#5-Mostra tots els individus de l’exercici 4, què són majors d’edat i tenen un pes igual o superior a la mitjana.
sumPes=0

for x in lista:
    sumPes+= x['pes']

mitjana=round(sumPes/len(lista), 2)

print(f"El total de la mitjana de pesos és {mitjana} kg")

for elem in lista:
    if elem['edat']>=18:
        if elem['pes']>=mitjana:
            print(f"Aquestes són les dades: {elem['nom']} {elem['cognom']} {elem['edat']} {elem['pes']} {elem['major']}")

