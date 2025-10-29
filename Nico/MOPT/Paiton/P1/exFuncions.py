'''1- Crea una funció longituds que a partir d’una llista de paraules i una longitud, retorni tres valors: quantes paraules tenen la mateixa longitud,  quantes una longitud inferior i quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon)
'''
llista_paraules = ["Hola","Adeu","Quatre","Cinc"]
def longituds(paraules,longitud):
    igual = 0
    menos = 0
    mas = 0
    for i in paraules:
        if len(i) == longitud:
            igual += 1
        elif len(i) > longitud:
            mas += 1
        else:
            menos += 1
    print(f"La llista es aquesta: {paraules}")
    print(f"La longitud introduida es {longitud}")
    print(f"Hi ha {igual} paraules d'igual longitud")
    print(f"Hi ha {menos} paraules de menor longitud")
    print(f"Hi ha {mas} paraules de major longitud")

longituds(llista_paraules,4)

'''

2- Crea una funció puntsDaus que a partir d’una llista de valors de tirades de daus, calculi una puntuació de la següent manera:
Si hi ha algun dau que sigui menor que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Se sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.

puntuacio=puntsDaus(punts)

'''
tirades_daus = [1,5,4,5,2,3,3,3,3]
tirades_daus2 = [3,3,3,3,3]
def punts_daus(tirades):
    suma = 0
    daumenor = False
    for i in tirades:
        suma += i
        if i < 3:
            daumenor = True
        elif i == 6:
            suma += 1
    
    print(f"La puntuacio final es {0 if daumenor else suma}")

punts_daus(tirades_daus)


'''

3- Crea una funció valorsRang que a partir d’una llista de valors, un valor mínim i un valor màxim, retorni una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats per teclat (inclosos), sense valors repetits.

escollits=valorsRang(llista, valmin, valmax)

'''
llista_valors = [1,2,3,4,5,6]
def valors_rang(llista,min,max):
    nova_llista = []
    for i in llista:
        if i >= min and i <= max and i not in nova_llista:
            nova_llista.append(i)
    print(f"La nova llista es \n {nova_llista}")

valors_rang(llista_valors,2,5)






'''

4- Crea una funció calcula_segons que calculi la quantitat de segons en un temps donat en hores, minuts i segons.
segons = calcula_segons( hores, minuts, segons)
'''
def calcula_segons(hores,minuts,segons):
    res = hores*3600 + minuts*60 + segons
    print(f"Segons: {res}")

calcula_segons(1,1,1)


'''


5- Crea una funció temps que calculi la quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)
'''
def temps(segons:int):
    hores:int = segons/3600
    minuts:int = (segons%3600)/60
    seg:int = (segons%3600)%60
    
    print(f"En {segons:.0f} segons hi ha {hores:.0f} hores, {minuts:.0f} minuts i {seg:.0f} segons")
    
temps(3661)
    


'''

6- Escriu una funció esvocal que a partir un caràcter torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)
'''

def es_vocal(caracter:str):
    vocals = ["A","E","I","O","U"]
    if caracter.capitalize() in vocals:
        print("Es una vocal")
    else:
        print("No es vocal")

es_vocal("a")


'''



7-Crea una funció canviaMorse programa que sigui capaç de transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat a https://es.wikipedia.org/wiki/Código_morse.

8-Crea una funció diferencies que a partir de dues cadenes de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"]

9-Crea una funció comptaLA que a partir d'una frase retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4

Exemple:
Ell s'ha passat la tarda cantant LaLAlA, ...
Retorna 4

10-Crea una funció comptaLES que a partir d'una frase retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3
'''