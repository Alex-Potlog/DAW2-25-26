#while - El fem servir quan sabem que en algun moment hem de parar
    #Exemple 1
i = 1
while i < 6:
    print(i)
    i += 1

    #Exemple 2
z = 1
while z < 6:
    print(z)
    z += 1
else:
    print("i is no longer less than 6")

#for - El fem servir quan hem de recorrer tot els elements, quan hem d'anar a inici a fi
    # Puc fer: llista, range (i++)

rang1=range(21)
for i in rang1:
    print(i)

print("-----------------------------------------")
rang2=range(2, 21)
for i in rang2:
    print(i)

print("-----------------------------------------")
rang3=range(2,21,3)
for i in rang3:
    print(i)

print("-----------------------------------------")
#per posar els nombres un al costat de l'altre 
llista=[]
rang4=range(2,31,4)
for i in rang4:
    llista.append(i)

for valor in llista:
    print(valor, end=' ')