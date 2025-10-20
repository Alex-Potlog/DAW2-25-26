# 1-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
# Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.

llista1 = [45, -6, 0, -32, 23, 9]

llista2 = []
for i in llista1:
    llista2.append(abs(i))
print("Llista absoluta: "+", ".join(map(str,llista2)))

# 2-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
# Mostra per consola els valors de la llista sense repetir cap. Fes servir un bucle i un tipus set.


llista3 = [45, -6, 0, -32, 45, -6, 0, -32]
llista4 = set()

for i in llista3:
    llista4.add(i) 

print("Llista absoluta: "+", ".join(map(str,llista4)))


# 3-Crea una llista amb contingut de tipus str, amb diverses paraules.
# Mostra les paraules començant per l’inici de la llista i començant pel final.

llista5 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print("Normal: ")
for i in llista5:
    print(i, end=' ')
print()
print("Invertida:  ")
for i in range(len(llista5)):
    print(llista5[(i*-1)-1], end=' ')
print()
    