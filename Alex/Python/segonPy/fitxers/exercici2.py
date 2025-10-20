def concatena(arxiu1, arxiu2):
    try:
        with open(arxiu1, "") as base, open(arxiu2, "r") as sobre:
            print(arxiu1)
    except FileNotFoundError as e:
        print(f"S'ha produït una excepció: {e.__str__().capitalize()}")
    

concatena("fitxer.txt", "fitxer2.txt")