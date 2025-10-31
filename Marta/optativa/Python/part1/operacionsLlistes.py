llista= [3, 24, 5, 7, 6, 2, 0, 9]

#DEMANAR A L'USUARI
#Afegir (append)
llista.append(15)
print(llista)

#Eliminar (remove)
llista.remove(5)
print(llista)

#Suma dels 4 mes grans
llista.sort()
suma=llista[-1]+llista[-2]+llista[-3]+llista[-4]
print(llista)
print(suma)

#Afegir a una posició x [dins del rang] (insert)
llista.insert(3,5)
print(llista)

#Eliminar la posició x afegida en el punt anterior (pop)
llista.pop(3)
print(llista)

#"Slie" d'una llista
llista2= llista [2:5]
print(llista2)