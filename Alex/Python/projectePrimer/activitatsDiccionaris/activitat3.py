# Programa per agrupar tirades de dos daus pel mateix valor

# Inicialitzem el diccionari
tirades = {}

# Recorrem totes les possibles combinacions de dos daus (1-6)
for dau1 in range(1, 7):
    for dau2 in range(1, 7):
        # Calculem la suma dels dos daus
        suma = dau1 + dau2
        
        # Si la suma ja està al diccionari, afegim la tirada
        if suma in tirades:
            tirades[suma].append([dau1, dau2])
        # Si no està, creem una nova llista amb la tirada
        else:
            tirades[suma] = [[dau1, dau2]]

# Mostrem el resultat
print("Resultat:")
print(tirades)