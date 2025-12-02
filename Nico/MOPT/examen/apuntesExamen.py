'''
1-Demana per teclat una quantitat i a continuació entra 
per teclat diversos noms fins a la quantitat entrada. 
Al final mostra tots els noms per pantalla.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Mortadelo Filemón
'''

#versió amb bucle for

quantitat=int(input("Entra quantitat: "))

llista=[]

for i in range(1,quantitat+1):
    nom=input("nom "+str(i)+" ? ")
    llista.append(nom)

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')

print()

#versió amb bucle while

quantitat=int(input("Entra quantitat: "))

llista=[]
i=0
while i<quantitat:
    i=i+1
    nom=input("nom "+str(i)+" ?")
    llista.append(nom)

print("Els noms són:", end=' ')
i=0
while i<len(llista):
    print(llista[i], end=' ')
    i=i+1

'''
2-Igual a l’exercici 1, però sense permetre noms repetits.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
Repetit, nom 3 ? Sacarino
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Filemón Sacarino
'''

quantitat=int(input("Entra quantitat: "))

llista=[]

i=1
while i<=quantitat:
    nom=input("nom "+str(i)+" ? ")
    if nom in llista:
        # Repetit
        print("Repetit,", end='')
    else:
        # Nou
        llista.append(nom)
        i=i+1

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')
    
'''
3-Crea un diccionari, amb diverses dades d’un individu, 
seguint aquesta estructura:

{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

Demana les dades per teclat i mostra la informació al final. 
Si l’individu és major d’edat, afegeix “(major d’edat)”.
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
Aquestes són les dades: Arenita Mejillas 19 anys 1.1 Kg (major d’edat)
'''

nom=input("Entra el nom: ")
cognom=input("Entra el cognom: ")
edat=int(input("Entra edat: "))
pes=float(input("Entra pes: "))

dades={"nom": nom , "cognom": cognom, "edat": edat , "pes": pes}

print(dades["nom"], dades["cognom"], dades["edat"], "anys", 
      dades["pes"], "Kg", end='')

if dades["edat"]>=18:
    print(" (major d'edat)")
    
'''
4-Crea una llista (list) de diccionaris com els de l’exercici 3. 
No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
Mostra el contingut de tota la llista segons s’indica a l’exercici 3.
Mostra la quantitat d’individus majors d’edat.
Mostra la mitjana del pes de tots els individus.
Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.
'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

majors=0  # comptabilitza els majors d'edat
sumapes=0; # suma de tots els pesos per càlcul de la mitjana
apareguts=list() # llista de noms apareguts
repetits=set() # set de noms repetits

for dades in llista:
    print(dades["nom"], dades["cognom"], dades["edat"], "anys", 
        dades["pes"], "Kg", end='')
    if dades["edat"]>=18:
        print(" (major d'edat)")
        majors=majors+1
    else:
        # S'ha de fer salt de línia si no és major d'edat
        print()
    sumapes=sumapes+dades["pes"]
    if dades["nom"] in apareguts:
        # És un nom repetit
        repetits.add(dades["nom"])
    else:
        # És la primera vegada que surt el nom
        apareguts.append(dades["nom"])
        
mitjana=sumapes/len(llista)
print("Hi ha",majors, "individus majors d'edat")
print("La mitjana dels pesos és", mitjana, "Kg")
if len(repetits)==0:
    print("SENSE NOMS REPETITS")
else:
    print("Els nom repetits són: ", repetits)


'''
5-Mostra tots els individus de l’exercici 4, què són majors d’edat i 
tenen un pes igual o superior a la mitjana.

'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

sumapes=0; # suma de tots els pesos per càlcul de la mitjana

for dades in llista:
    sumapes=sumapes+dades["pes"]
        
mitjana=sumapes/len(llista)
print("La mitjana dels pesos és", mitjana, "Kg")

for dades in llista:
    if dades["edat"]>=18 and dades["pes"]>=mitjana:
        print(dades["nom"], dades["cognom"], dades["edat"], "anys", 
            dades["pes"], "Kg", end='')
        if dades["edat"]>=18:
            print(" (major d'edat)")
        else:
            # S'ha de fer salt de línia si no és major d'edat
            print()


'''
1-Crea una llista de valors numèrics enters, no fa falta
llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, 
però modificant tots els valors negatius per el seu valor en 
positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
'''

llista1=[45, -6, 0, -32, 23, 9]

llista2=[]
for n in llista1:
    if n<0: n=-n
    llista2.append(n)

print("Llista 1:", llista1)
print("Llista 2:", llista2)


'''
2-Crea una llista de valors numèrics enters, no fa falta 
llegir-la del teclat.
Mostra per consola els valors de la llista sense repetir cap.
Fes servir un bucle i un tipus set.
Exemple:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Resultat:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Sense repetits: -32 -6 0 45 23 9
'''

llista1=[45, -6, 0, -32, -6, 0, 45, 45, 23, 9]

norepetits=set()

for n in llista1:
    norepetits.add(n)

print("Llista:", llista1)
print("Sense repetits:", norepetits)

'''
3-Crea una llista amb contingut de tipus str, amb diverses 
paraules.
Mostra les paraules començant per l’inici de la llista i 
començant pel final.
Utilitza bucles.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
the quick brown fox jumps over the lazy dog
dog lazy the over jumps fox brown quick the
'''

llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for n in llista1:
    print(n, end=' ')

print()

for n in llista1[-1::-1]:
    print(n, end=' ')

'''
4-Seguint l’exercici 3, mostra les paraules 
de posicions parelles i posicions senars.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
parelles: the brown jumps the dog
senars: quick fox over lazy
'''

llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

print("parelles:", end=' ')
for n in llista1[::2]:
    print(n, end=' ')

print()
print("senars:", end=' ')
for n in llista1[1::2]:
    print(n, end=' ')

'''
5-Seguint l’exercici 1, mostra una tercera llista 
amb els enters parells de la llista 2.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
Llista 3: [6, 0, 32]
'''

llista1=[45, -6, 0, -32, 22, 9]
llista2=[]
llista3=[]

for n in llista1:
    if n<0:
        n=-n
    llista2.append(n)
    if n%2==0:
        llista3.append(n)

print("Llista 1:", llista1)
print("Llista 2:", llista2)
print("Llista 3:", llista3)

'''
6- Crea una list de 100 enters, omple'l amb els
números de l'1 al 100 i després mostra'ls.
'''

llista=list(range(1,101))

for n in llista:
    print(n, end=' ')
    
'''
7- Crea una list de 100 enters, omple'l amb els
números del 101 al 200 i després mostra'ls.
'''

llista=list(range(101,201))

for n in llista:
    print(n, end=' ')

'''
8- Mostra la taula de multiplicar d’un nombre entrat per teclat. 
El programa ha de validar que el valor entrat estigui entre 1 i 10. 
Si no ho està, repeteix la pregunta.
Sortida del programa:
---------------------------------------
Quina taula vols veure (1-10)? : 15
Quina taula vols veure (1-10)? : 0
Quina taula vols veure (1-10)? : 4

TAULA DEL 4
=============
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
'''

taula=0
while taula<1 or taula>10:
    taula=int(input("Quina taula vols veure (1-10)? : "))

print()
print("TAULA DEL", taula)
print("=============")
for i in range(1,11):
    print(taula, "*", i, "=", i*taula)

'''
9- Tenim una list amb strings(str) amb noms i cognoms, com per exemple:
"Angel","Cuesta","Eva","López","Pol","Castro" 
on cada nom va seguit del seu cognom. 
Mostra les dades per consola de manera que surti un nom i el seu 
cognom a cada línia.
Exemple:
Angel Cuesta
Eva López
Pol Castro
'''

nomcognoms=["Angel","Cuesta","Eva","López","Pol","Castro"]

for i in range(0,len(nomcognoms),2):
    nom, cognom = nomcognoms[i:i+2]
    print(nom, cognom)
'''
1-Calcula amb un diccionari la freqüència d'aparició de vocals en una frase (suposem que no fem servir accents).
Exemple:
Entra frase: les vocals son aeiou
Resultat:
{'e':2, 'o':3, 'a':2, 'i':1, 'u':1}
'''

vocals={}

frase=input("Entra una frase: ")

for lletra in frase:
    if lletra in vocals:
        # Si la lletra és dins del diccionari es tracta d'una vocal
        vocals[lletra]+=1
    else:
        # La lletra no és al diccionari, s'afegeix si és una vocal
        if lletra in "aeiou":
            vocals[lletra]=1

print(vocals)

'''
2-Calcula amb un diccionari la freqüència d'aparició de números en una llista i les posicions a on apareixen.
Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
Entra llista: 1 -4 3 1 1 5 7 7
Resultat:
{1:[0,3,4], -4:[1], 3:[2], 5:[5], 7:[6,7]}
'''

posicions={}

valors=input("Entra la llista: ")
llista=list(map(int, valors.split(" ")))

p=0  # Serveix per saber la posició de cada valor
for num in llista:
    if num in posicions:
        # num és dins del diccionari, guardem la posició a la seva llista
        posicions[num].append(p)
    else:
        # num no és al diccionari, afegim num a la posició p
        posicions[num]=[p]  # el valor és una llista
    p=p+1 # avancem a la següent posició
  
print(posicions)

'''
3-De totes les possibles tirades de dos daus, agrupa-les pel mateix valor.
Resultat:
{2: [[1, 1]], 3: [[1, 2], [2, 1]], 4: [[1, 3], [2, 2], [3, 1]], ... , 12: [[6, 6]]}
'''

tirades={}

for dau1 in range(1,7):
    for dau2 in range(1,7):
        tirada=dau1+dau2
        if tirada in tirades:
            tirades[tirada].append([dau1,dau2])
        else:
            tirades[tirada]=[[dau1,dau2]]

print(tirades)

'''
4-D'una llista de valors, crea un histograma gràfic.
Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
Entra llista: 1 -4 3 1 1 5 2 2 7 7 -2 3 3 3
Resultat:
-4 *
-3
-2 *
-1
 0
 1 ***
 2 **
 3 ****
 4
 5 *
 6
 7 **
'''

valors=input("Entra llista: ")
llista=list(map(int, valors.split(" ")))
llista.sort()
histograma={}
m=min(llista)
M=max(llista)
for n in llista:
    if n in histograma:
        histograma[n]+=1
    else:
        histograma[n]=1

for n in range(m, M+1):
    print("{0:3d}".format(n), '*' * histograma.get(n, 0))

'''
Modifica l'exercici 1 de bucles i llistes per a fer servir una funció:

Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]

#Solució actual:
llista1=[45, -6, 0, -32, 23, 9]

llista2=[]
for n in llista1:
    if n<0: n=-n
    llista2.append(n)

print("Llista 1:", llista1)
print("Llista 2:", llista2)

Es tracta de fer el mateix amb una funció:

llista1=[45, -6, 0, -32, 23, 9]
llista2=senseNegatius(llista1)
print("Llista 1:", llista1)
print("Llista 2:", llista2)
'''

def senseNegatius(llista):
    llista2=[]
    for n in llista:
        if n<0: n=-n
        llista2.append(n)
    return llista2

llista1=[45, -6, 0, -32, 23, 9]
llista2=senseNegatius(llista1)
print("Llista 1:", llista1)
print("Llista 2:", llista2)


'''
Modifica l'exercici 3 de bucles i llistes per a fer servir una funció:

Crea una llista amb contingut de tipus str, amb diverses paraules.
Mostra les paraules començant per l’inici de la llista i començant pel final.
Utilitza bucles.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
the quick brown fox jumps over the lazy dog
dog lazy the over jumps fox brown quick the

#Solució actual:
llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for n in llista1:
    print(n, end=' ')

print()

for n in llista1[-1::-1]:
    print(n, end=' ')

Es tracta de fer el mateix amb una funció:
llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
llista2=inversa(llista1)
print(llista1)
print(llista2)
'''

def inversa(llista):
    llista2=[]
    for n in llista[-1::-1]:
        llista2.append(n)
    return llista2

def mostra(llista):
    for n in llista:
        print(n, end=' ')
    print()
    
llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
llista2=inversa(llista1)
mostra(llista1)
mostra(llista2)
'''
1- Crea una funció longituds que a partir d’una llista 
de paraules i una longitud, retorni tres valors: 
quantes paraules tenen la mateixa longitud,  
quantes una longitud inferior i 
quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon)
'''

def longituds(paraules, lon):
    iguals=0
    grans=0
    petites=0
    for p in paraules:
        if len(p)==lon:
            iguals+=1
        else:
            if len(p)>lon:
                grans+=1
            else:
                petites+=1
    return iguals, petites, grans


#Exemples d'utilització
paraules=["proves", "exercicis", "prog"]

iguals6, petites6, grans6 = longituds(paraules, 6)
print(iguals6, petites6, grans6)

iguals7, petites7, grans7 = longituds(paraules, 7)
print(iguals7, petites7, grans7)

print(longituds(paraules, 10))

'''
2- Crea una funció puntsDaus que a partir d’una llista 
de valors de tirades de daus, calculi una puntuació 
de la següent manera:
Si hi ha algun dau que sigui menor 
que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Se sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.

puntuacio=puntsDaus(punts)
'''

def puntsDaus(punts):
    puntuacio=0
    if 1 not in punts and 2 not in punts:
        sis=0
        for p in punts:
            puntuacio+=p
            if p==6: sis+=1
        if puntuacio>12: puntuacio+=2
        puntuacio+=sis
    return puntuacio


#Exemples d'utilització
daus=[5, 6, 2, 5, 6]
p=puntsDaus(daus)
print(p)

p=puntsDaus([5, 6, 4, 5, 6])
print(p)

p=puntsDaus([5, 5, 5, 6])
print(p)

print(puntsDaus([5, 6, 4, 5, 6]))

'''
3- Crea una funció valorsRang que a partir d’una llista de valors, 
un valor mínim i un valor màxim, 
retorni una nova llista amb tots els valors de la primera 
què es troben entre els dos valors entrats per teclat (inclosos), 
sense valors repetits.

escollits=valorsRang(llista, valmin, valmax)
'''

def valorsRang(llista, valmin, valmax):
    escollits=set()
    for n in llista:
        if n>=valmin and n<=valmax:
            escollits.add(n)
    return list(escollits)

#Exemples d'utilització
llista=[4, 6, 2, -3, 0, 3, 3, 7]
nova=valorsRang(llista, 2, 7)
print(nova)

'''
4- Crea una funció calcula_segons que calculi 
la quantitat de segons en un temps donat en hores, minuts i segons.
segons = calcula_segons( hores, minuts, segons)
'''

def calcula_segons( hores, minuts, segons):
    return (hores*60+minuts)*60+segons

#Exemples d'utilització
# 00:10:05  -->  605 seg
print(calcula_segons( 0, 10, 5))

'''
5- Crea una funció temps que calculi la 
quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)
'''

def temps(segons):
    negatiu=False
    if segons<0:
        segons=-segons
        negatiu=True
    minuts=segons//60
    segons=segons%60
    hores=minuts//60
    minuts=minuts%60
    if negatiu: return -hores, -minuts, -segons
    return hores, minuts, segons

#Exemples d'utilització
#605 seg   -->  00:10:05
hores, minuts, segons = temps(605)
print(hores, minuts, segons)

#3661 seg  -->  01:01:01
print (temps(3661))

h,m,s =temps(1000)
print (calcula_segons(h,m,s))  

'''
6- Escriu una funció esvocal que a partir un caràcter 
torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)
'''

def esvocal(caracter):
    return caracter.lower() in "aeiouáéíóúàèìòùäëïöü"

#Exemples d'utilització
print(esvocal('A'))
print(esvocal('É'))
print(esvocal('Ë'))
print(esvocal('Ò'))
print(esvocal('i'))
print(esvocal('à'))
print(esvocal('J'))
print(esvocal('ñ'))

'''
7-Crea una funció canviaMorse programa que sigui capaç de 
transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i 
realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir 
un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat 
a https://es.wikipedia.org/wiki/Código_morse.
'''

def esMorse(missatge):
    for c in missatge:
        if c not in [' ','-','.']: return False
    return True

def obtenirMorse(missatge, codi):
    paraules=missatge.upper().split(' ')
    resultat=''
    for p in paraules:
        for c in p:
            resultat += codi.get(c,'')
            resultat += ' '
        resultat += ' '
    return resultat.strip()

def obtenirFrase(missatge, codi):
    paraules=missatge.split('  ')
    resultat=''
    for p in paraules:
        codis=p.split(' ')
        for c in codis:
            resultat += codi.get(c,'')
        resultat += ' '
    return resultat.strip()
    
def canviaMorse(missatge):
    lletra2morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'CH': '----', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 
    'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '"': '.-..-.', '/': '-..-.'
    }
    morse2lletra=dict(zip(lletra2morse.values(),lletra2morse.keys()))
    if esMorse(missatge):
        return obtenirFrase(missatge, morse2lletra)
    else:
        return obtenirMorse(missatge, lletra2morse)

print(canviaMorse("SOS"))
print(canviaMorse("Programacio de scripts"))
print(canviaMorse(canviaMorse("SOS")))
print(canviaMorse(canviaMorse("Programacio de scripts")))


'''
8-Crea una funció diferencies que a partir de dues cadenes 
de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i 
retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"]
'''

def diferencies(frase1, frase2):
    if (len(frase1)!=len(frase2)): return None
    llista=[]
    for i in range(len(frase1)):
        if frase1[i]!=frase2[i]:
            llista.append(frase2[i])
    return llista

print(diferencies("Em dic mouredev", "Em dic meuredov"))
print(diferencies("Em dic.Brais Moure", "Em dic brais moure"))

'''
9-Crea una funció comptaLA que a partir d'una frase 
retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4

Exemple:
Ell s'ha passat la tarda cantant LaLAlA, ...
Retorna 4
'''

def comptaLA(frase):
    compt=0
    for i in range(len(frase)-1):
        if frase[i:i+2].lower()=="la":
            compt += 1
    return compt

print(comptaLA("Ell s'ha passat la tarda cantant La, LA, lA, ..."))
print(comptaLA("Ell s'ha passat la tarda cantant LaLAlA, ..."))

'''
10-Crea una funció comptaLES que a partir d'una frase 
retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3
'''

def comptaLES(frase):
    compt=0
    for i in range(len(frase)-2):
        if frase[i:i+3].lower()=="les":
            compt += 1
    return compt

print(comptaLES("Ell es passa totes les tardes cantant LaLESlesla..."))

'''
1- Crea un script per realitzar còpia de seguretat de diversos orígens.
Farà falta una funció per a fer la còpia d'un origen a un destí.
def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.
L'script tindrà una variable amb la llista d'orígens que s'han de copiar i 
una altra variable amb el destí de les còpies.
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
import os
import shutil

def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.
    try:
        print("Còpia des de", origen, "a", desti)
        if os.path.isdir(origen): 
            shutil.copytree(origen, desti, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(desti), exist_ok=True)
            shutil.copy2(origen, desti)
    except FileNotFoundError as e:
        print("No existeix", origen)

if __name__=='__main__':
    origens=['/home/informatica/.ssh', 
             '/home/informatica/Documentos/', 
             '/home/informatica/Descargas/empresa.mwb',
             '/dades',
             'Exercici1.py'
             ]
    
    desti='/home/informatica/copies/'
    for org in origens:
        if org[0]=='/': nomDesti=os.path.join(desti, org[1:])
        else: nomDesti=os.path.join(desti, org)
        copiaDades(org, nomDesti)


'''
2- Crea un script per realitzar la restauració de la còpia de seguretat anterior.
L'script tindrà dues variables: origen de les còpies i destí de restauració.
copies='/copies/'  # Fan falta drets de lectura
desti='/proves/'  # Fan falta drets d'escriptura

Funcions útils:
os.listdir(path)  Ex:  llista=os.listdir('/copies')
'''
import os
from .Exercici1 import copiaDades

if __name__=='__main__':
    copies='/home/informatica/copies/'
    desti='/home/informatica/proves/'
    copiaDades(copies, desti)

'''
3- Modifica els scripts per permetre tenir diverses còpies. 
Es tracta d'afegir una variable amb la quantitat de còpies a conservar. 
S'hauran de crear diversos directoris amb les còpies.
S'han de conservar la quantitat de còpies indicades, sempre les últimes n còpies fetes. 
En fer la restauració farà falta saber quina és la còpia que volem restaurar.
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
 
Si ja hem completat totes les possibles còpies i en volem 
fer una més, s'haurà de sobreescriure la més antiga.

Funcions útils:
os.path.getmtime(path)
os.path.isdir(path)
'''

import os, time, shutil
from Exercici1 import copiaDades

def ncopia(desti, ncopies):
    '''
    Detecta quin és el directori de còpies més antic
    '''
    data_min=time.gmtime()
    copia_min=0
    for n in range(1,ncopies+1):
        ndesti=os.path.join(desti, str(n))
        if os.path.exists(ndesti) and os.path.isdir(ndesti):
            fhora=os.path.join(ndesti, "__hora__.txt")
            if os.path.exists(fhora):
                data=time.gmtime(os.path.getmtime(fhora))
            else:
                data=time.gmtime(os.path.getmtime(ndesti))
            if data<data_min:
                copia_min=n
                data_min=data
        else:
            return n
    return copia_min

if __name__=='__main__':
    origens=['/home/informatica/.ssh', 
             '/home/informatica/Documentos/', 
             '/home/informatica/Descargas/empresa.mwb',
             '/dades',
             'Exercici1.py'
             ]
    
    desti='/home/informatica/copies/'
    ncopies=5
    ncopia=ncopia(desti, ncopies)
    for org in origens:
        nomDesti=os.path.join(desti, str(ncopia))
        if os.path.exists(nomDesti): shutil.rmtree(nomDesti)
        if org[0]=='/': nomDestiCopia=os.path.join(nomDesti, org[1:])
        else: nomDestiCopia=os.path.join(nomDesti, org)
        copiaDades(org, nomDestiCopia)
        open(os.path.join(nomDesti, "__hora__.txt"), 'a')


'''
4- Unifica els scripts i selecciona la tasca a realitzar 
segons els paràmetres que rebi.
Nom script: filesadm.py

Paràmetres:
-h --help            Missatge informatiu del funcionament.
-b --backup          Fa la còpia de seguretat.
-r --restore         Recupera l'última còpia guardada.
-R num --restn num   Recupera la còpia amb número num.
-d path --dest path  Destí de les còpies de seguretat.
-n num               Quantitat de còpies de seguretat guardades.
-o --overwrite       Permet sobreescriure les dades guardades o recuperades.
'''

import getopt, sys, os, shutil
from Exercici1 import copiaDades
from Exercici3 import ncopia

def usage():
    print('Funcionament:\n'
            +'-h --help             Missatge informatiu del funcionament.\n'
            +'-b --backup           Fa la còpia de seguretat.\n'
            +'-r --restore          Recupera l\'última còpia guardada.\n'
            +'-R num --restn num    Recupera la còpia amb número num.\n'
            +'-d path --dest path   Destí de les còpies de seguretat.\n'
            +'-n num                Quantitat de còpies de seguretat guardades.\n'
            +'-o --overwrite        Permet sobreescriure les dades guardades o recuperades.\n')

origens=['/home/informatica/proves/', 
         '/home/informatica/Descargas/empresa.mwb',
         '/dades',
         ]
    
def main():
    maxcopies=5
    copia=0
    desti=None
    volemRestore=volemBackup=False
    overwrite=False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hbrR:d:n:o", ["help", "backup", "restore", "restn=", "dest=", "overwrite"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    if not opts:
        #Si no té cap opció, mostra help
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--overwrite"):
            overwrite=True
        elif o in ("-d", "--dest"):
            desti=a
        elif o in ("-n", "--num"):
            maxcopies=int(a)
        elif o in ("-r", "--restore"):
            if not volemBackup: volemRestore=True
        elif o in ("-b", "--backup"):
            if not volemRestore: volemBackup=True
        elif o in ("-R", "--restn"):
            a=int(a)
            if a>0 and not volemBackup:
                copia=a
                volemRestore=True
        else:
            assert False, "unhandled option"
        
    if (volemBackup or volemRestore) and not desti:
        print("Falta el path destí.")
        sys.exit()
    
    if volemBackup and desti:
        # Còpia del procediment de l'exercici 3
        copia=ncopia(desti, maxcopies)
        nomDesti=os.path.join(desti, str(copia))
        if os.path.exists(nomDesti):
            if overwrite:
                shutil.rmtree(nomDesti)
            else:
                print("Existeix", nomDesti, "i no hi ha overwrite activat.")
                sys.exit()
        for org in origens:
            if org[0]=='/': nomDestiCopia=os.path.join(nomDesti, org[1:])
            else: nomDestiCopia=os.path.join(nomDesti, org)
            copiaDades(org, nomDestiCopia)
            open(os.path.join(nomDesti, "__hora__.txt"), 'a')
        
    if volemRestore and desti:
        # Per defecte fa restore de la còpia 1
        if copia==0: copia=1
        nomOrg=os.path.join(desti, str(copia))
        if not os.path.exists(nomOrg):
            print("No s'ha trobat la còpia", nomOrg)
            sys.exit()
        for dst in origens:
            if dst[0]=='/': nomOrgCopia=os.path.join(nomOrg, dst[1:])
            else: nomOrgCopia=os.path.join(nomOrg, dst)
            copiaDades(nomOrgCopia, dst)

if __name__ == "__main__":
    main()
    
    
'''
5- Crea un script que accepti els següents paràmetres:
-m --missatge         Mostra el text "Missatge de prova"
-f text --frase text  Mostra "FRASE: " i el text passat per paràmetre
-h --help             Mostra informació sobre com fer servir aquest script
'''

import getopt, sys

def usage():
    print('Funcionament:\n'
        +'-m --missatge          Mostra el text "Missatge de prova"\n'
        +'-f text --frase text   Mostra "FRASE: " i el text passat per paràmetre\n'
        +'-h --help              Mostra informació sobre com fer servir aquest script')
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "mf:h", ["missatge", "frase=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    if not opts and not args:
        #Si no té cap opció, mostra help
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--frase"):
            print("FRASE: "+a)
            sys.exit()
        elif o in ("-m", "--missatge"):
            print("Missatge de prova")
            sys.exit()
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()


'''
6- Crea un script que mostri el contingut d'un directori passat per paràmetre.
'''

import getopt, sys, os

def usage():
    print('Funcionament:\n'
        +'-d dir  --directory dir Mostra el contingut del directori\n'
        +'-h --help               Mostra informació sobre com fer servir aquest script')
 
def mostraDir(path):
    if not path: return
    if os.path.exists(path) and os.path.isdir(path):
        for f in os.listdir(path):
            print(f)
    else:
        print("No és un directori")
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h", ["directory=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--directory"):
            mostraDir(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: mostraDir(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


'''
7- Crea un script que faci la creació d'un directori amb el nom passat per paràmetre.
'''

import getopt, sys, os

def usage():
    print('Funcionament:\n'
        +'-d dir  --mkdir dir  Crea un directori amb el nom indicat\n'
        +'-h --help            Mostra informació sobre com fer servir aquest script')
 
def creaDir(path):
    if not path: return
    if os.path.exists(path) and os.path.isfile(path):
        print("Existeix un fitxer amb el mateix nom")
    else:
        os.makedirs(path, exist_ok=True)
        print("S'ha creat el directori",path)
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h", ["mkdir=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--mkdir"):
            creaDir(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: creaDir(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


'''
8- Crea un script que mostri la data de creació d'un fitxer o directori passat per paràmetre.
'''

import getopt, sys, os, time

def usage():
    print('Funcionament:\n'
        +'-s element --source element  Mostra la data de l\'element amb el nom indicat\n'
        +'-h --help                    Mostra informació sobre com fer servir aquest script')
 
def mostraData(path):
    if not path: return
    if not os.path.exists(path):
        print("No existeix", path)
    else:
        print(path, time.strftime("%c", 
                time.gmtime(os.path.getmtime(path))))
    
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:h", ["source=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--source"):
            mostraData(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: mostraData(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


