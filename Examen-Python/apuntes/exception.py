try:
    # Codigo que pot generar una excepció
    resultat = 10 / 1
except ZeroDivisionError as e:
    # Captura i maneig de l'excepció
    print(f"S'ha produït una excepció: {e.__str__().capitalize()}")
else:
    # Codi que s'executa si no hi ha excepcions
    print(f"El resultat és: {resultat}")
finally:
    # Codi que s'executa sempre, independentment de si hi ha hagut una excepció o no
    print("Execució finalitzada.")