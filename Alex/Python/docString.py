import random

def atac_critic(dany: int) -> int:
    """Retorna el dany, aquest pot ser critic.
    
    Args:
        dany (int): Dany base de l'atac.
        
    Returns:
        int: Dany total després de considerar si és crític o no.
    """
    es_critic = int(random.random() * 5) == 0
    if es_critic:
        return (dany * 2)
    return dany

def tirar(dice_notation: str, k: int = 1):
    """Tira els daus segons la notació donada i retorna estadístiques.
    Args:
        dice_notation (str): Notació dels daus en format 'XdY', on X és la quantitat de daus i Y el nombre de cares.
        k (int, optional): Nombre de vegades que es vol tirar els daus. Per defecte és 1.
    Returns:
        dict: Diccionari amb la mitjana i el màxim resultat obtingut.
    """
    llistadaus = dice_notation.split("d")
    quantitat = int(llistadaus[0])
    daus = int(llistadaus[1])
    tirades = []
    maxim = 0
    mitjana = 0
    for _ in range(k):
        tirada = 0
        for i in range(quantitat):
            tirada = int(random.random() * daus) + 1
            print(f"Acaba de sortir el {tirada}!")
            tirades.append(tirada)
            if tirada > maxim:
                maxim = tirada
            mitjana += tirada
    mitjana = mitjana / (quantitat * k)
    resultats = {
        "mitjana": mitjana,
        "maxim": maxim
    }
    return resultats

help(atac_critic)
help(tirar)