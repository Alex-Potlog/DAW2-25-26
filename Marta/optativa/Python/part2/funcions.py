""" def nom_fun ():
    .....
    .....
    ..... """

#Exemple 1:
def senseNeg (lista1):
    lista2=[]

    for elem in lista1:
        if elem<0:
            lista2.append(abs(elem))
        else:
            lista2.append(elem)
    
    return lista2


lista1=[45, -6, 0, -32, 23, 9]
lista2=senseNeg(lista1)

print(lista2)
print("------------------------------------------------------------------")

#Exemple 2
def inversa(listaStr):
    listaStr2=[]
    i=len(listaStr)-1
    separa=" "

    while i>=0:
        listaStr2.append(listaStr[i])
        i-=1
    
    return listaStr2


listaStr=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
listaStr2=inversa(listaStr)

print(listaStr)
print(listaStr2)
print("------------------------------------------------------------------")