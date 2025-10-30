#tupla -> com les llistes ordenades, no mutable ja que no puc canviar el valor un cop introduit, permet dublicats i es poden afegir

#dict (de diccionari)-> conjunt de clau valor, es mutable, no permet duplicats, no es indexable

#set -> valor no ordenable, mutable, indexable, no permet duplicats

#frozenset -> no ordenat, pot ser una llista



#1. Crea una llista amb els números del 1 al 5 i
lista = []
rang4=range(1,6)
for i in rang4:
    lista.append(i)

'''for valor in lista:
    print(valor, end=' ')'''

# Afegeix el numero 6
lista.append(6)
print(lista)

# Elimina el número 3 i el nombre de la posició 3
lista.remove(3)
print(lista)

lista.pop(3)
print(lista)

# Mostra el primer i l'últim
print(f"El primer: {lista[0]}, i l'últim: {lista[-1]}")

# 2. Converteix la llista [10, 20, 30] en una cadena de text "10-20-30"
lista2=[10, 20, 30]
print(str(lista2[0])+"-"+str(lista2[1])+"-"+str(lista2[2]))

#3. Escriu un programa que donada una llista de paraules, imprimex només les que tingui 4 lletres
listaPalabra= ["dos", "tres", "millor", "nau", "María"]

