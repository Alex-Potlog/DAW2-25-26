# Programa per crear un histograma gràfic d'una llista de valors

frase = input("Entra llista: ")

# Convertim la frase en una llista d'enters
llista = list(map(int, frase.split(" ")))

# Creem un diccionari per comptar les freqüències
frequencia = {}

for num in llista:
    if num in frequencia:
        frequencia[num] = frequencia[num] + 1
    else:
        frequencia[num] = 1

# Trobem el valor mínim i màxim per mostrar tots els números del rang
minim = min(llista)
maxim = max(llista)

# Mostrem el resultat
print("Resultat:")
for num in range(minim, maxim + 1):
    # Si el número està a la llista, mostrem els asteriscs
    if num in frequencia:
        print(f"{num} {'*' * frequencia[num]}")
    # Si no està, només mostrem el número
    else:
        print(num)