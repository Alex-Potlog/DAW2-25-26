def mostra(nom):
    try:
        with open("fitxer.txt", "r") as arxiu:
            print(arxiu.read())
    except FileNotFoundError as e:
        print(f"S'ha produït una excepció: {e.__str__().capitalize()}")
    finally:
        arxiu.close

#fitxer = input("Entra el nom del fitxer: ")
mostra("fitxer.txt")