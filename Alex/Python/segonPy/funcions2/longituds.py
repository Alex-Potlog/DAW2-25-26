def longituds (paraules, lon):
    
    mesures = {
        "grans": 0,
        "iguals": 0,
        "petits": 0
    }
    
    if type(paraules) is list and type(lon) is int:
        for i in paraules:
            if len(i) == lon:
                mesures["iguals"] += 1
            elif len(i) > lon:
                mesures["grans"] += 1
            else:
                mesures["petits"] += 1
    return mesures


llista = [
    "paraguas",
    "manzana",
    "yasuo",
    "coma",
    "azul",
    "patrañas",
    "supercalifragilisticospialidoso",
    "Michael"
]

result = longituds(llista, 4)

print(result)