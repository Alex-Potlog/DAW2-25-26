"""1-Calcula amb un diccionari la freqüència d'aparició de vocals en una frase (suposem que no fem servir accents).
Exemple:
Entra frase: les vocals son aeiou
Resultat:
{'e':2, 'o':3, 'a':2, 'i':1, 'u':1}"""

# Demanem la frase a l'usuari
frase = input("Entra frase: ").lower()

# Creem un diccionari amb les vocals
vocals = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

# Comptem les aparicions de cada vocal
for lletra in frase:
    if lletra in vocals:
        vocals[lletra] += 1

# Mostrem el resultat
print("Resultat:")
print(vocals)

"""2-Calcula amb un diccionari la freqüència d'aparició de números en una llista i les posicions a on apareixen.
Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
Entra llista: 1 -4 3 1 1 5 7 7
Resultat:
{1:[0,3,4], -4:[1], 3:[2], 5:[5], 7:[6,7]}"""
# Demanem la llista a l'usuari
entrada = input("Entra llista: ")
llista = list(map(int, entrada.split()))

# Diccionari per emmagatzemar números i les seves posicions
freq_posicions = {}

# Recorrem la llista amb les seves posicions
for i, num in enumerate(llista):
    if num in freq_posicions:
        freq_posicions[num].append(i)
    else:
        freq_posicions[num] = [i]

# Mostrem el resultat
print("Resultat:")
print(freq_posicions)


"""
3-De totes les possibles tirades de dos daus, agrupa-les pel mateix valor.
Resultat:
{2: [[1, 1]], 3: [[1, 2], [2, 1]], 4: [[1, 3], [2, 2], [3, 1]], ... , 12: [[6, 6]]}

"""


diccionari = {}

for i in range(2,13):
    diccionari_temp ={i:[]}
    diccionari.update(diccionari_temp)

for j in range(1,7):
    for k in range(1,7):
        suma = j+k
        llista_temp =[j,k]
        resultat = diccionari[suma]
        resultat.append(llista_temp)

        diccionari[suma] = resultat

print( diccionari)

"""
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
 """

introduit=""
numeros = input("Introdueix números separats per espais: ")

llista = list(map(int, numeros.split()))

diccionari2={}
for element in llista:
    if element in diccionari2.keys():
        info =diccionari2[element]
        info += "*"
        diccionari2[element] = info
    else:
        diccionari_temp2 = {element:"*"}
        diccionari2.update(diccionari_temp2)

for i in range(min(diccionari2.keys()),max(diccionari2.keys())+1):
    if i not in diccionari2.keys():
        dict_temp = {i:""}
        diccionari2.update(dict_temp)

for key in sorted(diccionari2.keys()):  
    print(f"{key:} {diccionari2[key]}")

print(diccionari2)