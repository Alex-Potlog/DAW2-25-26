import datetime
""" 1- Crea una funció longituds que a partir d’una llista de paraules i una longitud, retorni tres valors: quantes paraules tenen la mateixa longitud,  quantes una longitud inferior i quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon) """

def longituds (lista, long):
    countIgual=0
    countMenys=0
    countMes=0

    for m in lista:
        longitudParaula= len(m) 
        if longitudParaula>long:
            countMes+=1
        elif longitudParaula<long: 
            countMenys+=1
        else:
            countIgual+=1
    
    return countIgual, countMenys, countMes

lista=["Fent", "servir", "un", "bucle", "compta", "les", "paraules", "de", "la", "llista", "que", "tenen", "la", "mateixa", "longitud"]

long=6

countIgual, countMenys, countMes=longituds(lista, long)

print(f"Longitud igual a {long}: {countIgual}")
print(f"Longitud inferior a {long}: {countMenys}")
print(f"Longitud superior a {long}: {countMes}")
print("----------------------------------------------------------")

""" 2- Crea una funció puntsDaus que a partir d’una llista de valors de tirades de daus, calculi una puntuació de la següent manera:
Si hi ha algun dau que sigui menor que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Se sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6. 

puntuacio=puntsDaus(punts)"""

def puntsDaus (punts):
    puntuacio=0

    for m in punts:
        if m<3:
            puntuacio=0
        elif m==6:
            puntuacio+=m+1
        else:
            puntuacio+=m
            if puntuacio>12:
                puntuacio+=2
        
    return puntuacio

punts=[4, 5, 4]

puntuacio=puntsDaus(punts)

print(puntuacio)

print("----------------------------------------------------------")
""" 3- Crea una funció valorsRang que a partir d’una llista de valors, un valor mínim i un valor màxim, retorni una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats per teclat (inclosos), sense valors repetits.

escollits=valorsRang(llista, valmin, valmax) """

def valorsRang (llistaValors, valMin, valMax):
    escollits=set()

    for m in llistaValors:
        if m>=valMin and m<=valMax:
            escollits.add(m)
    
    return escollits

llistaValors=[5,-2, 120, 55, 68, -13, 16, 41, 32, -98]
valMin=int(input("Entra valor minim: "))
valMax=int(input("Entra valor màxim: "))

escollits=valorsRang(llistaValors, valMin, valMax)

print(escollits)
print("----------------------------------------------------------")
""" 4- Crea una funció calcula_segons que calculi la quantitat de segons en un temps donat en hores, minuts i segons.
segons = calcula_segons( hores, minuts, segons) """

def calculaSegons(hores, minuts, segons):
    calcMin=hores*60
    mins=minuts+calcMin
    calcSegons=mins*60
    segonsTotals=segons+calcSegons

    return segonsTotals

x=datetime.datetime.now()

hores=int(x.strftime("%H"))
minuts=int(x.strftime("%M"))
segons=int(x.strftime("%S"))
print(hores, minuts, segons)

seconds=calculaSegons(hores, minuts, segons)
print(seconds)

""" 5- Crea una funció temps que calculi la quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons) """

def temps(segons):
    minuts=segons//60
    restoSegons=segons%60
    hores=minuts//60
    restoMinuts=minuts%60

    return (hores, restoMinuts, restoSegons)

segons= 7257

calculSeg=temps(segons)

print(calculSeg)

""" 6- Escriu una funció esvocal que a partir un caràcter torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”) """

def esVocal(caracter):
    match (caracter):
        case 'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U':
            return (caracter, "és una vocal")
        case _:
            return (caracter, "NO és una vocal")
        

caracter="A"

vocal=esVocal(caracter)

print(vocal)

"""7 -Crea una funció canviaMorse programa que sigui capaç de transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat a https://es.wikipedia.org/wiki/Código_morse. """

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N':'-.', 'Ñ':'--.--',
    'O':'---', 'P':'.--.', 'Q': '--.-', 'R':'.-.', 'S': '...',
    'T': '-', 'U':'..-', 'V': '...-', 'W':'.--', 'X':'-..-',
    'Y': '-.--', 'Z': '--..'
}

#morse_dict = {
#    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
#    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
#   ... etc
#}
#
# all(c in '.- ' for c in text)
#
# split(' ') // split('  ')
#
#  text_dict = {v: k for k, v in morse_dict.items()}
# 
#  def canviaMorse(text):
    # 1. Detectar tipus
#    if es_morse(text):
#        return morse_a_text(text)
#    else:
#        return text_a_morse(text)  #


""" 8-Crea una funció diferencies que a partir de dues cadenes de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"] """

def diferencies(text1, text2):

    text3=[]
    longMinim=min(len(text1), len(text2))
        
    for i in range(longMinim):
        if text1[i] !=text2[i]:
            text3.append(text2[i])
    
    # Afegir caràcters restants si text2 és més llarga
    if len(text2) > len(text1):
        for i in range(len(text1), len(text2)):
            text3.append(text2[i])

    return text3

text1="Em dic Marta"
text2="Em dic Carla"

textDif=diferencies(text1, text2)

print (textDif)

""" 9-Crea una funció comptaLA que a partir d'una frase retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4 """

def comptaLA (cadena, busca):
    frase=cadena.upper()
    compt=0
    i=0
    
    for i in range (len(frase)-1):
        if frase[i:i+2]=="LA":
            compt+=1

    return "S'han trobat "+ str(compt)+" vegades"

cadena="Ell s'ha passat la tarda cantant La, LA, lA, ..."
busca="LA"

cuentaLA=comptaLA(cadena, busca)
print (cuentaLA)

""" 10-Crea una funció comptaLES que a partir d'una frase retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3 """

def comptaLES (cadena, busca):
    frase=cadena.upper()
    compt2=0
    i=0
    
    for i in range (len(frase)-1):
        if frase[i:i+3]=="LES":
            compt2+=1

    return "S'han trobat "+ str(compt2)+" vegades"

cadena="Ell es passa totes les tardes cantant LaLESlesla..."
busca="LES"

cuentaLES=comptaLES(cadena, busca)
print (cuentaLES)
