a='Hola Món!'
print(a)

#En el cas de cadenes de text, això no es pot fer -> EXEMPLE
#a[1]='J'

#upper y lower per a majuscula i minuscules
    #Exemple de "upper"
txt = "Hello my friends"
x = txt.upper()
print(x)

    #Exemple de "lower"
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#split() em convertes els elements d'una cadena en una cadena
txt = "welcome to the jungle"
x = txt.split()
print(x)

#join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#replace('valorAntic', 'valorNou') -> EXEMPLE replace('l', 'J')
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#slice() per a tallar una cadena
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

#Per concatenar cadenes farem servir el +
