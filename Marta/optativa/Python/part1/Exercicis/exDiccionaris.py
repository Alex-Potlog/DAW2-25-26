#1-Calcula amb un diccionari la freqüència d'aparició de vocals en una frase (suposem que no fem servir accents).
    # Exemple: Entra frase: les vocals son aeiou
    # Resultat: {'e':2, 'o':3, 'a':2, 'i':1, 'u':1}
frase=input("Escriu una frase: ")

listFrase=frase.split()

print(listFrase)

countE=0
countO=0
countA=0
countI=0
countU=0
myDicFrase=dict()

for m in listFrase:
    for lletra in m:
        if lletra=="e" or lletra=="E":
            countE+=1
        elif lletra=="o" or lletra=="O":
            countO+=1
        elif lletra=="a" or lletra=="A":
            countA+=1
        elif lletra=="i" or lletra=="I":
            countI+=1
        elif lletra=="u" or lletra=="U":
            countU+=1
    
    myDicFrase['e']=countE
    myDicFrase['o']=countO
    myDicFrase['a']=countA
    myDicFrase['i']=countI
    myDicFrase['u']=countU

print(myDicFrase)
print("------------------------------------------------------------------")
# 2-Calcula amb un diccionari la freqüència d'aparició de números en una llista i les posicions a on apareixen.
    # Exemple: (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" "))) 
    # Entra llista: 1 -4 3 1 1 5 7 7
    # Resultat: {1:[0,3,4], -4:[1], 3:[2], 5:[5], 7:[6,7]}

frase2="1 -4 3 1 1 5 7 7"
listaNum=list(map(int, frase2.split(" ")))

print(listaNum)

myDicPosicio=dict()

for p, num in enumerate(listaNum):
    if num in myDicPosicio:
        myDicPosicio[num].append(p)
    else:
        myDicPosicio[num]= [p]

print(myDicPosicio)
print("------------------------------------------------------------------")
# 3-De totes les possibles tirades de dos daus, agrupa-les pel mateix valor.
    # Resultat: {2: [[1, 1]], 3: [[1, 2], [2, 1]], 4: [[1, 3], [2, 2], [3, 1]], ... , 12: [[6, 6]]}

myDicDaus=dict()

for dau1 in range (1, 7):
    for dau2 in range (1,7):
        suma= dau1 + dau2
        if suma in myDicDaus:
            myDicDaus[suma].append([dau1, dau2])
        else:
            myDicDaus[suma]=[[dau1, dau2]]


print(myDicDaus)
print("------------------------------------------------------------------")
# 4-D'una llista de valors, crea un histograma gràfic.
    # Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
    # Entra llista: 1 -4 3 1 1 5 2 2 7 7 -2 3 3 3
    # Resultat:
'''-4 *
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
        7 **'''

frase3="1 -4 3 1 1 5 2 2 7 7 -2 3 3 3"
listaNum2=list(map(int, frase3.split(" ")))

#listaNum2.sort()
# print(listaNum2)

minim=min(listaNum2)
maxim=max(listaNum2)

for a in range(minim, maxim +1):
    count=listaNum2.count(a)
    if count>0:
        print(f"{a} {'*'*count}")
    else:
        print(a)