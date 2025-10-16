# Programa per calcular la freqüència i posicions de números en una llista

frase = input("Entra llista: ")

# Convertim la frase en una llista d'enters
llista = list(map(int, frase.split(" ")))

# Inicialitzem el diccionari per guardar les posicions
posicions = {}

# Recorrem la llista amb índex i valor
for i, num in enumerate(llista):
    # Si el número ja està al diccionari, afegim la nova posició
    if num in posicions:
        posicions[num].append(i)
    # Si no està, creem una nova llista amb la posició actual
    else:
        posicions[num] = [i]

# Mostrem el resultat
print("Resultat:")
print(posicions)