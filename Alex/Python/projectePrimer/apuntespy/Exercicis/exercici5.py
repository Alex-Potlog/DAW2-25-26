# 1-Demana per teclat una quantitat i a continuació entra per teclat diversos noms fins a la quantitat entrada. Al final mostra tots els noms per pantalla.

# noms = []
# quantitat = int(input("Entra quantitat: "))
# for i in range(quantitat):
#     noms.append(input(f"{i+1}, Entra nom: "))
# print("Els noms són: "+" ".join(map(str,noms)))

# 2-Igual a l’exercici 1, però sense permetre noms repetits.

# noms = []
# quantitat = int(input("Entra quantitat: "))
# for i in range(quantitat):
#     comprovat = False
#     while(not comprovat):
#         nom = input(f"{i+1}, Entra nom: ")
#         if ((nom not in noms)):
#             noms.append(nom)
#             comprovat = True
#         else:
#             print("Repetit, ")
# print("Els noms són: "+" ".join(map(str,noms)))

#3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:

persona = {
    "nom": str(input("Entra nom: ")),
    "cognom": str(input("Entra cognom: ")),
    "edat": int(input("Entra edat: ")),
    "pes": float(input("Entra pes: "))
}

print(f"Aquestes són les dades: {persona["nom"]} {persona["cognom"]} {persona["edat"]} anys {persona["pes"]}KG {"" if persona["edat"]<18 else "(major d'edat)"}")
                                                                                                                                                
# 4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.

classe = [
    {"nom": "Calamardo","cognom": "Tentaculos","edat": 21,"pes": 12.5},
    {"nom": "Bob","cognom": "Esponja","edat": 15,"pes": 7},
    {"nom": "Arenita","cognom": "Mejillas","edat": 18,"pes": 9},
    {"nom": "Arenita","cognom": "Mejillas","edat": 14,"pes": 9}
]

# majors = 0
# for i in classe:
#     if (classe['edat']>=18):
#         majors = majors + 1
#     print("Els noms són: "+" ".join(map(str,classe)))
    



# print("Mitjana de pes: ")