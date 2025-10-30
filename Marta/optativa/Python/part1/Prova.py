print ("HOLA")

nom = input ("Marta")

print(type (nom)) #Per saber el tipus de variable que tinc.

print (nom)

num1= int (input ("fica número "))

sep = ' '; #variable 

# Tipus de dades: int, float, complexe (exemple: 2f), string, boolean, 
# diccionari (conjunt de dades que tinc guardades a algu lloc), llistes, duplas, rangs

num1= int(input ("Entra un numero: "))
num2= int(input ("Entra numero dos: "))
suma=num1+num2
print(suma)
#QUant a mes a mes vull afegir un text a davant, ho he de convertir i fer-ho de la següent manera
print("EL resultat es "+str(suma))
#L'altre versió es fer el "print f" de java
print(f"El resultat es: {suma}")
# {suma.2f}: per afegir els decimals que vull que m'aparegui per pantalla

# Quan guardo un valor a una variable puc sumar, restar, multiplicar, dividir, 
# elevar al quadrat (necessito el següent per elevar el quadrat: **), l'arrel quadrada (necessitem: **0,5)

sum=25
print(f"L'arrel quadrada de {sum} es {sum**0.5}")

# Per a comentar una sola linia he de fer servir el coixinet (#) i 
# si vull comentar varies linees fare servir 3 cometes (''') - puc primer escriure, despres sel·leccionar 
# i escriure llavors les 3 cometes
'''gfssgdfsddsg
gsgsddsgdgs'''

# OPCIONS and/or (==, !=, >, <, ...)
# CONDICIONS
# if (condició):
#   print("")

if suma==25:
    print (suma**0.5)
else:
    print (suma)

#Exemple 2 del if...else
numA= int(input ("Entra un numero: "))

if numA>0:
    print("El nombre és més gran a 0")
elif numA<0:
    print("Nombre més petit a 0")
else:
    print("Nombre igual a 0")

#Exemple and:
nota = int(input("Introdueix la nota "))

if nota:
    if nota>=0 and nota<5:
        print("Suspès")
    elif nota>=5 and nota<=7:
        print("Aprovat")
    else:
        print("Excel·lent")

#Llistes (ve a ser una array de java)
llista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c']

print(llista[0])

#modificar cadena
llista[2]='m'
print(llista[2])

#append - m'afageix un element al final de la llista
llista.append(600)
print(llista)

#remove - m'elimina el primer element que de la llista que em coincideixi 
    #(és a dir, si tinc la següent llista [1,2,3,2,4,4,1], i escric llista.remove(2) m'eliminarà el primer 2 que es trobi)
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

#sort - ordena la llista
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#llista[-1] - em dóna l'últim element de la llista
fruits = ['apple', 'banana', 'cherry']
print(fruits[-1])

#insert - per inserir un element a la llista 
    #llista.insert (2,15) - insereixo a la posició 2 el numero 15
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop - em elimina el valor de la posició que jo li indico entre parentesis. En el cas de no existir la poisició indicada error.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#len() - em dóna quants elements tinc en una llista
mylist = ["apple", "orange", "cherry"]
x = len(mylist)
print(x)

#En una nova llista puc afegir els elements d'una llista original. Exemple: Si tinc la llista[2,4,3,6] 
    # i creo una llista nova de la següent manera -> llista2= llista[1:3] ens agafarà un tros de la llista, concretament m'agafarà
    #els elements de les posicions 1 i 2, el de la posició 3 NO
lista1=[2,4,6,7]
lista2=lista1[1:3]
print(lista2)