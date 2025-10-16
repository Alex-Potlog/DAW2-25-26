'''Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu.
Mostra les dues llistes per consola.
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
llista1 = [-3,-2,-1,0,1,2,3]
def sense_negatius(llista):
    llista2 = []
    for n in llista:
        llista2.append(abs(n))
    return print(f"Llista 1: {llista}\nLlista 2: {llista2}")

sense_negatius(llista1)

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
print(llista2)'''
llista1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
def revertir_llista(llista):
    llista2 = []
    for n in llista[-1::-1]:
        llista2.append(n)
    return llista2

print(llista1)
print(revertir_llista(llista1))