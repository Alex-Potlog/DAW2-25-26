# En aquest codi es mostra com s'afegeix a una linia
def escriuPos(fitxer, frase, linia):
    try:
        # Llegir totes les línies
        with open(fitxer, 'r') as file:
            linies = file.readlines()
        
        # Comprovar si la línia és vàlida
        if linia < 0 or linia >= len(linies):
            print(f"Error: La línia {linia} no existeix. El fitxer té {len(linies)} línies.")
            return
        
        # Substituir la línia
        linies[linia] = frase + '\n'
        
        # Reescriure tot el fitxer
        with open(fitxer, 'w') as file:
            file.writelines(linies)
        
        print(f"Frase escrita a la línia {linia} correctament.")
        
    except FileNotFoundError:
        print(f"Error: El fitxer '{fitxer}' no existeix.")
    except Exception as e:
        print(f"Error inesperat: {e}")


# Exemple d'ús:
frase = 'Bon dia a la vila del pingüí'
linia = 2  # Tercera línia (si comences des de 0)
escriuPos('exemple3.txt', frase, linia)