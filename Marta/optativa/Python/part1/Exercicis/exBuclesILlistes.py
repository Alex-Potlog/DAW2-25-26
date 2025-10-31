#1-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
#Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant
# tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
        #Exemple: Llista 1: [45, -6, 0, -32, 23, 9]
        # Resultat:
        # Llista 1: [45, -6, 0, -32, 23, 9]
        # Llista 2: [45, 6, 0, 32, 23, 9]

lista1=[45, -6, 0, -32, 23, 9]
lista2=[]
for elem in lista1:
    if elem < 0:
        lista2.append(abs(elem))
    else:
        lista2.append(elem)

print(lista2)
print("------------------------------------------------------------------")
#2-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
# Mostra per consola els valors de la llista sense repetir cap. Fes servir un bucle i un tipus set.
        #Exemple: Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
        # Resultat:
        # Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
        # Sense repetits: -32 -6 0 45 23 9

listaEnters=[45, -6, 0, -32, -6, 0, 45, 45, 23, 9]

listaNoRepe=[]

for elem in listaEnters:
    if elem not in listaNoRepe:
        listaNoRepe.append(elem)

print(f"Els nombres sense repetir són {listaNoRepe}")
print("------------------------------------------------------------------")
# 3-Crea una llista amb contingut de tipus str, amb diverses paraules. Mostra les paraules començant 
# per l’inici de la llista i començant pel final. Utilitza bucles.
    #Exemple: Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    # Resultat:
    # the quick brown fox jumps over the lazy dog
    # dog lazy the over jumps fox brown quick the

listaParaula= ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

separa=" "

# Es mostra per pantalla des de la primera a l'útlima
k=0

frase=""
while k<len(listaParaula):
    paraula=listaParaula[k]
    frase+=paraula+separa
    k+=1

print(frase)

#(També podem fer servir frase=separa.join(listaParaula) // print(frase))

# Es mostra per pantalla des de l'última a la primera
i=len(listaParaula)-1

frasee=""
while i>=0:
    paraula=listaParaula[i]
    frasee+=paraula+separa
    i-=1

print(frasee)
print("------------------------------------------------------------------")
# 4-Seguint l’exercici 3, mostra les paraules de posicions parelles i posicions senars.
    # Exemple: Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    # Resultat:
    # parelles: the brown jumps the dog
    # senars: quick fox over lazy
listaParaula= ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
l=0

separa=" "
fra=""
frase2=""
while l<len(listaParaula):
    if l%2==0:
        paraula=listaParaula[l]
        fra+=paraula+separa
    else:
        para=listaParaula[l]
        frase2+=para+separa
    l+=1

print(fra)
print(frase2)
print("------------------------------------------------------------------")
#5-Seguint l’exercici 1, mostra una tercera llista amb els enters parells de la llista 2.
    #Exemple: Llista 1: [45, -6, 0, -32, 23, 9]
    #Resultat:
    #Llista 1: [45, -6, 0, -32, 23, 9]
    #Llista 2: [45, 6, 0, 32, 23, 9]
    #Llista 3: [6, 0, 32]
lista1=[45, -6, 0, -32, 23, 9]
lista2=[]
lista3=[]
for elem in lista1:
    if elem < 0:
        lista2.append(abs(elem))
    else:
        lista2.append(elem)
    

for elem in lista2:
    if elem%2==0:
        lista3.append(elem)


print(lista1)
print(lista2)
print(lista3)
print("------------------------------------------------------------------")
# 6- Crea una list de 100 enters, omple'l amb els números de l'1 al 100 i després mostra'ls.
listaCien=[]

c=1

while c<=100:
    listaCien.append(c)
    c+=1

print(listaCien)
print("------------------------------------------------------------------")
# 7- Crea una list de 100 enters, omple'l amb els números del 101 al 200 i després mostra'ls.
listaCien2=[]

cc=101

while cc<=200:
    listaCien2.append(cc)
    cc+=1

print(listaCien2)
print("------------------------------------------------------------------")

# 8- Mostra la taula de multiplicar d’un nombre entrat per teclat. El programa ha de validar que el valor entrat estigui entre 1 i 10. Si no ho està, repeteix la pregunta.
#Sortida del programa:
#---------------------------------------
#Quina taula vols veure (1-10)? : 15
#Quina taula vols veure (1-10)? : 0
#Quina taula vols veure (1-10)? : 4

#TAULA DEL 4
#=============
#4 * 1 = 4
#4 * 2 = 8
#4 * 3 = 12
#4 * 4 = 16
#4 * 5 = 20
#4 * 6 = 24
#4 * 7 = 28
#4 * 8 = 32
#4 * 9 = 36
#4 * 10 = 40

num=int(input("Quina taula vols veure (1-10)? : "))

while num<1 or num>10:
    num=int(input("Quina taula vols veure (1-10)? : "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

print("------------------------------------------------------------------")
# 9- Tenim una list amb strings(str) amb noms i cognoms, com per exemple: "Angel","Cuesta","Eva","López","Pol","Castro"
# on cada nom va seguit del seu cognom.
# Mostra les dades per consola de manera que surti un nom i el seu cognom a cada línia.
        # Exemple:
        # Angel Cuesta
        # Eva López
        # Pol Castro

listNoms= ["Angel","Cuesta","Eva","López","Pol","Castro"]

n=0

while n<len(listNoms):
    nombre=listNoms[n]+" "+listNoms[n+1]
    print(nombre)
    n+=2
