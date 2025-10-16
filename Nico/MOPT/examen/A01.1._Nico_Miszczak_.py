''' 
|----------------------------------------------------|
| Nom:Nicolas                                        |
| Cognoms:Miszczak                                   |
| Grup:DAW2                                          |
| Data:7/10/25                                       |
|----------------------------------------------------|
Agrupa tots els exercicis en un únic fitxer A01.1_NOM_COGNOM.py. Posa un comentari a l’inici de cada exercici
indicant quin és. Els exercicis han de funcionar amb qualsevol conjunt de dades de prova.
1-(2,5p) Crea una list amb paraules diverses, directament al codi.
Demana per teclat una longitud de paraula (quantitat de caràcters).
Fent servir un bucle, compta les paraules de la llista que tenen la mateixa longitud, les que tenen
una longitud inferior i les que tenen una longitud superior.
Mostra el resultat.
Nota: per obtenir la longitud d’una paraula es pot fer servir len(paraula)
Exemple:
list →
"Fent",
"servir",
"un",
"bucle",
"compta",
"les",
"paraules",
"de",
"la",
"llista",
"que",
"tenen",
"la",
"mateixa",
"longitud"
longitud 6
longitud igual a 6: 3
longitud inferior a 6: 9
longitud superior a 6: 3
'''
print("Exercici 1")
llistaParaules = ["hola","adios","perro","elefante","gato"]
lon = int(input("Quantes lletres (int)?"))
igual = 0
menos = 0
mas = 0
for i in llistaParaules:
    print(i)
    if len(i) == lon:
        igual += 1
    elif len(i) > lon:
        mas += 1
    else:
        menos += 1

print(f"Longitud:{lon}")
print(f"longitud igual a {lon}: {igual}")
print(f"longitud inferior a {lon}: {menos}")
print(f"longitud superior a {lon}: {mas}")

'''

2-(2,5p) Realitza un joc de daus en els qual es guanyen uns punts en funció del resultat de diversos daus tirats. Si hi ha algun dau que sigui menor que 3,
aleshores la puntuació final és zero punts. En altre cas la puntuació es calcula de la següent manera:
Es sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.
Llegeix del teclat la quantitat de daus i a continuació el valor de tots els daus.
Calcula i mostra la puntuació corresponent.
Utilitza bucles.
Exemples:
3 Daus 3,6,3
Puntuació 13
3 Daus 4,3,6
Puntuació 16
5 Daus 1,1,3,6,1
Puntuació 0
4 Daus 6,6,4,3
Puntuació 23
'''
print("\nExercici 2")
qdaus = int(input("Quants daus?"))
suma = 0
daus = []
daumenor = False
for i in range(qdaus):
    daus.append(int(input(f"Valor del dau {i}:\n"))) #Se sobreentiende que es un dado o tenia que limitarlo por si hay algun oscar?
    
for i in daus:
    suma += i
    if i == 6:
        suma += 1
    if suma > 12:
        suma += 2
    if i < 3:
        daumenor = True
print(f"{qdaus} daus {daus}")
if daumenor:
    print("La puntuació es 0 (Havia un dau menor de 3)")
else:
    print(f"La puntuacio es {suma}")







'''

3-(2,5p) Crea una list amb valors enters, directament al codi.
Demana per teclat dos valors numèrics. Crea una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats per teclat (inclosos), 
sense valors repetits.
Mostra la nova llista. Utilitza bucles.
Exemple:
list → 5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100
Límits -10 a 20
Resultat:
5, 8, 0, -5, 20, 7, 9
'''
print("\nExercici 3")
listaentera = [1,2,3,4,5,6]
valor1 = int(input("Valor 1:\n"))
valor2 = int(input("Valor 2:\n"))
listamodificada = [] 
listaentera.sort() #No fa falta ordenar la llista pero queda millor
#ordenar per que valor 1 sigui el menor
if valor1 > valor2:
    aux = valor1
    valor1 = valor2
    valor2 = aux

for i in listaentera:
    if i >= valor1 and i <= valor2 and i not in listamodificada: #no volem valors repetits
        listamodificada.append(i)
print(listamodificada)
print(f"Valors limit: {valor1}:{valor2}")






'''

4-(2,5p) Fent servir el següent diccionari: edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}. 
Crea un bucle que demani per teclat diversos valors clau (key), fins que el valor sigui 'FI'. 
Per cada clau, si existeix al diccionari, mostra un missatge amb el valor que li correspon. 
Si no existeix, demana per teclat un valor i afegeix la clau:valor al diccionari.
Mostra el diccionari final.
Exemple:
Entra clau: Bob
Bob té 26
Entra clau: Clint
Nou valor: 99
Entra clau: Nate
Nate té 89
Entra clau: Katie
Katie té 47
Entra clau: Tom
Nou valor: 65
Entra clau: FI
Resultat:
{'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate':89, 'Clint': 99, 'Tom': 65}

''' 
print("\nExercici 4")
edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}
clau = ""
while clau != "Fi":
    clau = input("Introdueix clau:\n")
    
    #edats.get(clau)
    
    #Se que no es asi, no se me ocurria otra cosa ahora mismo
    for persones in edats:
        if persones == clau:
            #print(f" {clau} Existeix")
            print(f"{clau} te {edats[clau]}")
        else:
            print("No me acuerdo como añadir a un diccionario")
            
print(f"Resultat:\n{edats}")