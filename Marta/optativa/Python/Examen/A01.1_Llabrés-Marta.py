#EXERCICI 1 --------------------------------------------------------------------------

lista=["Fent", "servir", "un", "bucle", "compta", "les", "paraules", "de", "la",
"llista", "que", "tenen", "la", "mateixa", "longitud"]

#print(lista) -> print que mostra la llista per consola

longitud=int(input("Entra la longitud: ")) #Variable per introduir la longitud desitjada

#Contadors que aniràn contant les paraules depenent de la seva longitud
countLong=0
countMenys=0
countMes=0

#Bucle for que recorre tota la llista de paraules, on la 'm' posició de la llista on es troba en aquell moment
for m in lista:
    longitudParaula= len(m) #Variable que em guarda la quantitat de caracters que té cada paraula
    #print(longitudParaula)
    if longitudParaula>longitud: #En el cas que la longitud de la paraula de la posició 'm' sigui més llarga que la longitud introduida per teclat, m'augmenta el contador indicat
        countMes+=1
    elif longitudParaula<longitud: #En el cas que la longitud de la paraula de la posició 'm' sigui més curta que la longitud introduida per teclat, m'augmenta el contador indicat
        countMenys+=1
    else: #En el cas de no complir cap de les condicions anteriors, m'augmenta el contador indicat
        countLong+=1

#Mostrem per pantalla cada contador amb el nombre de paraules corresponents segons la longitud introduit per consola
print(f"Longitud igual a {longitud}: {countLong}")
print(f"Longitud inferior a {longitud}: {countMenys}")
print(f"Longitud superior a {longitud}: {countMes}")




#EXERCICI 2 --------------------------------------------------------------------------
#Introduim a la variable el nombre de daus desitjats
numDaus=int(input("Nombre de daus: "))

i=1

listaEnter=[]

#Bucle que afegeix la llista els nombres introduits segons el nombre de daus llençats
while i<=numDaus:
    num=int(input(f"Numero del dau {i}: "))
    listaEnter.append(num)
    i+=1

sumaNum=0
#Bucle que realitza la suma dels nombres de la llista
for i in listaEnter:
    sumaNum+=i
    if i<3:
        i=0
    elif i==6:
        sumaNum+=1
    elif i==12:
        sumaNum+=2


print(f"{numDaus} Daus {listaEnter}")
print(f"Puntuació {sumaNum}")





#EXERCICI 3 --------------------------------------------------------------------------
'''listaNum=[5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100]

print(listaNum)

numInf=int(input("Introduiex el primer valor (inferior): "))
numSup=int(input("Introdueix el segon valor (superior): "))

novaListNum=[]



print(novaListNum)'''






#EXERCICI 4 --------------------------------------------------------------------------
edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

#S'introdueix la claus
valorClau=input("Entra clau: ")

#Bucle que fins que no s'introdueix la paraula 'fi', continua executant-se
# 
while valorClau!="Fi" and valorClau!="fi":
    if valorClau in edats:
        print(f"{valorClau} té {edats[valorClau]}")
    else:
        edats[valorClau]=int(input("Nou Valor: "))
    
    valorClau=input("Entra clau: ")

print(edats)
