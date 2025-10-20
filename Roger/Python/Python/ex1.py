# votants = int(input("Nombre de votants : "))
# enDretaVot = int(input("Nombre de gent que pot votar: "))
# afirmatius = int(input("Nombre de vots afirmatius: "))
# negatius = int(input("Nombre de vots negatius: "))

# participacio = (votants / enDretaVot) * 100
# print(f"Percentatge de participació: {participacio}%")

# percentatgeVotsAfirmatius = (afirmatius / votants) * 100
# print(f"Percentatge de vots afirmatius: {percentatgeVotsAfirmatius}%")

# percentatgeVotsNegatius = (negatius / votants) * 100
# print(f"Percentatge de votsnegatius{percentatgeVotsNegatius}%")

# percentatgeVotsEnBlanc = (votants - (afirmatius + negatius)) / votants

# if percentatgeVotsAfirmatius > 50:
#     print(f"Ha guanyat el sí{percentatgeVotsAfirmatius:2f}%")
# elif percentatgeVotsNegatius == 50:
#     print("Empat")
# else:
#     print("Ha guanyat el no")


# llista = [3,24,5,7,6,2,0,9]
# llista.append(int(input("Introdueix un número: ")))

# llista.remove(3)

# llista.sort()

# llista.upper()

llista2 =list(range(1,20,3))

print(llista2)

llista3 =[]
for valor in range(2,20,3):
    llista3.append(valor)

print(llista3)

llista4 =list(range(1,6))
llista4.append(6)

llista4.remove(3)

print(llista4[0],llista4[-1])

llista5 = list(range(0,31,10))

text=""

for i in llista5:
    if i==llista5[-1]:
        text+=str(i)
    else:
        text+=str(i)+"-"


print(text)

llista6 = ["casa","pou","arbre","cotxe"]


for paraula in llista6:
    if len(paraula)>=4:
        print(paraula)



tupla = (3,24,5,7,6,2,0,9) #tuples són immutables(no es poden modificar,si afegeir)

#Inicials
#1-Demana per teclat una quantitat i a continuació entra per teclat diversos noms fins a la quantitat entrada. Al final mostra tots els noms per pantalla.
# numero = int(input("Intodueix el numero d'elements"))
# llocs = ""

# for repeticio in range(0,(numero)):
#     paraula = str(input("Introdueix la paraula"))
#     llocs+=" "+paraula

# print(llocs)

#2-Igual a l’exercici 1, però sense permetre noms repetits.
# numero2 = int(input("Intodueix el numero d'elements"))
# llocs2 = [] 


# for repeticio in range(0,(numero2)):
#     paraula = str(input("Introdueix la paraula"))

#     if paraula in llocs2:
#         paraula=input("repetit")
#         repeticio-=1
#     else:
#         llocs2.append(paraula)
        

# print(llocs2)

"""3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:

{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

Demana les dades per teclat i mostra la informació al final. Si l’individu és major d’edat, afegeix “(major d’edat)”.

Exemple 1:

Entra nom: Bob Esponja

Entra cognom: SquarePants

Entra edat: 15

Entra pes: 0.2

Aquestes són les dades: Bob Esponja SquarePants 15 anys 0.2 Kg

Exemple 2:

Entra nom: Arenita

Entra cognom: Mejillas

Entra edat: 19

Entra pes: 1.1

Aquestes són les dades: Arenita Mejillas 19 anys 1.1 Kg (major d’edat)"""

individus = {"nom": "", "cognom": "", "edat": 0, "pes": 0.0}    
numero = input("Intodueix el numero d'elements")


for num in range(0,(numero)):
    individus["nom"] = input("Entra nom: ")
    individus["cognom"] = input("Entra cognom: ")
    individus["edat"] = int(input("Entra edat: "))
    individus["pes"] = float(input("Entra pes: "))

for individu in individus:
    if individus["edat"] >= 18:
        print(f"Aquestes són les dades{individus['nom']} {individus['cognom']} {individus['edat']} anys {individus['pes']} Kg (major d’edat)")
    else:
        print(f"Aquestes són les dades{individus['nom']} {individus['cognom']} {individus['edat']} anys {individus['pes']} Kg (menor d’edat)")

"""4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.

Mostra el contingut de tota la llista segons s’indica a l’exercici 3.

Mostra la quantitat d’individus majors d’edat.

Mostra la mitjana del pes de tots els individus.

Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”."""

individus2 = [
    {"nom": "Bob", "cognom": "Esponja", "edat": 15, "pes": 0.2},
    {"nom": "Arenita", "cognom": "Mejillas", "edat": 19, "pes": 1.1},
]

print(individus2)
print(f"Aquestes són les dades: {individus2[0]["nom"]} {individus2[0]["cognom"]} {individus2[0]["edat"]} anys {individus2[0]["pes"]} Kg")
print(f"Aquestes són les dades: {individus2[1]["nom"]} {individus2[1]["cognom"]} {individus2[1]["edat"]} anys {individus2[1]["pes"]} Kg ")

contador =0
for individu in individus2:
    if individu["edat"]>=18:
        contador+=1
print(f"Quantitat d’individus majors d’edat: {contador}")

sumaPes =0
for individu in individus2:
    sumaPes+=individu["pes"]

mitjanaPes = sumaPes / len(individus2)
print(f"Mitjana del pes de tots els individus: {mitjanaPes}")

nom =[]
nomsrepetit = []

for individu in individus2:
    if individu["nom"] in nom:
        nomsrepetit.append(individu["nom"])
    else:
        nom.append(individu["nom"])

if len(nomsrepetit)==0:
    print("SENSE NOMS REPETITS")
else:
    print(f"Noms què s’han repetit: {nomsrepetit}")

#5-Mostra tots els individus de l’exercici 4, què són majors d’edat i tenen un pes igual o superior a la mitjana. 

for individu in individus2:
    if individu["edat"]>=18 and individu["pes"]:
        print(f"Aquestes són les dades: {individu["nom"]} {individu["cognom"]} {individu["edat"]} anys {individu["pes"]} Kg \n")
