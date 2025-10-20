"""1-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]"""

llista1 = [45, -6, 0, -32, 23, 9]
llista2 = []

for element in llista1:
    element=abs(element)
    llista2.append(element)

print(llista2)

"""3-Crea una llista amb contingut de tipus str, amb diverses paraules.
Mostra les paraules començant per l’inici de la llista i començant pel final.
Utilitza bucles.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
the quick brown fox jumps over the lazy dog
dog lazy the over jumps fox brown quick the
"""

llista= ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for element in llista:
    print(element)

for element in llista[::-1]:
    print(element)

"""
8- Mostra la taula de multiplicar d’un nombre entrat per teclat. El programa ha de validar que el valor entrat estigui entre 1 i 10. Si no ho està, repeteix la pregunta.
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
"""
continuar = False
taula=0

while continuar==False:
    taula=int(input("Quina taula vols veure (1-10)? : "))

    if taula in range(1,10):
        continuar=True

print(f"Taula del {taula} \n")
for multiplicador in range(1,11):
    resultat = multiplicador*taula
    print(f"{taula}*{multiplicador} = {resultat}")