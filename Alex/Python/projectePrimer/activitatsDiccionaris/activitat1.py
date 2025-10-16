# Programa per calcular la freqüència d'aparició de vocals en una frase

frase = input("Entra frase: ")

# Definim les vocals (sense accents)
vocals = "aeiouAEIOU"

# Inicialitzem el diccionari per comptar les vocals
freq_vocals = {}

# Recorrem cada caràcter de la frase
for caracter in frase:
    # Comprovem si és una vocal
    if caracter in vocals:
        # Convertim a minúscula per no distingir majúscules
        vocal = caracter.lower()
        # Si ja està al diccionari, incrementem el comptador
        if vocal in freq_vocals:
            freq_vocals[vocal] = freq_vocals[vocal] + 1
        # Si no està, la inicialitzem amb 1
        else:
            freq_vocals[vocal] = 1

# Mostrem el resultat
print("Resultat:")
print(freq_vocals)