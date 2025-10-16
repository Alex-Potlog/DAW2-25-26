# Exercici 1
quant = int(input("Entra quantitat: "))

noms = []

for i in range(quant):
    nom = input("nom  " + str(i + 1) + " ? ")
    noms.append(nom)

print("Els noms son: ")
for i in range(len(noms)):
    print(noms[i], end=' ')

# Exercici 2
quant = int(input("Entra quantitat: "))

noms = []

cont = 0
while cont != quant:
    nom = input("nom  " + str(cont + 1) + " ? ")
    if nom not in noms:
        noms.append(nom)
        cont += 1
    else:
        print("Repetit.")

print("Els noms son: ")
for i in range(len(noms)):
    print(noms[i], end=' ')
    
# Exercici 3
persona = {
    "nom": input("Insereix el nom: "),
    "cognom": input("Insereix el cognom: "),
    "edat": int(input("Insereix l'edat: ")),
    "pes": float(input("Insereix pes: ")),
}

print("Aquestes son les dades: " + persona["nom"] + " " + persona["cognom"] + " " + str(persona["edat"]) + " " + str(persona["pes"]))

if persona["edat"] > 17:
    print("Major d'edat")


