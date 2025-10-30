'''
try:
    --------
exception:
    ----------------
else:
    ----------------
finally:

(la part del else i el finally és opcional)
'''

try:
    x=2/0
except:
    print("Entra en except, ja ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")
finally:
    print("Entra tot i que hi hagi una excepció")

#TIPUS D'EXCEPCIONS
#typeError
#valueError
#overflowError
#indexError
#KeyError
#nameError
#ImportError
#ZeroDivisionError

""" x=3
if x<0:
    raise Exception("Sorry, no numbers below zero")

x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
 """

''' Escriure programa que demani 2 nuemeros i mostra el resultat de la seva divisió.
Si s'introdueix com a divisor un 0, mostrar missatge d'error: "No es pot dividir per zero!"

afegeix un ValueError si l'usuari no introdueix nombres enters.
'''

num=int(input("Entra el primer número: "))
num2=int(input("Entra el segon número: "))

try:
    x=num/num2
except ZeroDivisionError:
    print(f"No es pot dividir per zero!")
if not type(x) is int:
    raise TypeError("No has introduit enters")
else:
    print(f"El resultat de dividir {num} entre {num2} és {x}")