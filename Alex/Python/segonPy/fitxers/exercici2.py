def concatena(arxiu1, arxiu2):
    try:
        # Llegir el contingut del primer arxiu
        with open(f"{arxiu1}", 'r', encoding='utf-8') as f1:
            contingut1 = f1.read()
        
        # Llegir el contingut del segon arxiu
        with open(f"{arxiu2}", 'r', encoding='utf-8') as f2:
            contingut2 = f2.read()
        
        # Concatenar els continguts
        contingut_concatenat = contingut1 + '\n' + contingut2
        
        # Mostrar el resultat
        print("Contingut concatenat:")
        print("-" * 40)
        print(contingut_concatenat)
        
        # Opcionalment, guardar el resultat en un nou arxiu
        with open("arxiu_concatenat.txt", 'w', encoding='utf-8') as f_sortida:
            f_sortida.write(contingut_concatenat)
        
        print("-" * 40)
        print("Arxius concatenats correctament! El resultat s'ha guardat a 'arxiu_concatenat.txt'")
        
    except FileNotFoundError as e:
        print(f"S'ha produït una excepció: {e.__str__().capitalize()}")
    

concatena("fitxer.txt", "fitxer2.txt")