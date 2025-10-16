#lista de 0 a 20
lista1 = []
for i in range(21):
    lista1.append(i)
print(lista1) 
# lista de 0 a 20 empezando por 2
lista2 = []
for i in range(19):
    lista2.append(i+2)
print(lista2)
#lista de 2 a 20 subiendo de 2 en 2
lista3 = []
for i in range(10):
    lista3.append((i*2)+2)
print(lista3)
#lista de 2 a 20 con salto de 3
lista4 = []
for i in range(7):
    lista4.append((i*3)+2)
print(lista4)


#crea lista con numeros del 1 al 5
lista5 = []
for i in range(5):
    lista5.append(i+1)
print(lista5)
# añade el 6
lista5.append(6)

# elimina el 3 y la 3a pos
lista5.remove(3)
lista5.pop(2)
print(lista5)

#muestra el primer y ultimo elemento
print(f"El primer element es {lista5[0]} i l'ultim es {lista5[-1]}")


#converteix la llista [10,20,30] en una cadena de text "10-20-30"
lista6 = [10,20,30]
cadena = ""
for i in range(len(lista6)):
    if i == len(lista6)-1:
        cadena += str(lista6[i])
    else:
        cadena += str(lista6[i]) + "-"
print(cadena)


#programa que donada una llista de paraules mostri nomes les que tinguin mes de 4 lletres
llistaParaules = ["hola","adios","perro","elefante","gato"]
for i in llistaParaules:
    if len(i) > 4:
        print(i)

