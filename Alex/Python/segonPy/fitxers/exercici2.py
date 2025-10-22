def concatena(arxiu1, arxiu2):
    try:
        with open(arxiu1, "r") as base:
            print(base.read())
            base.close
        with open(arxiu2, "r") as sobre:
            print(sobre.read())
        with open(arxiu1, "a+") as base:
            base.write(sobre)
            print(base.read())
    except FileNotFoundError as e:
        print(f"S'ha produït una excepció: {e.__str__().capitalize()}")
    

concatena("fitxer.txt", "fitxer2.txt")