def mostra():
    try:
        with open("exemple.txt", "r") as arxiu:
            print("Archivo en la línea 1: ", arxiu.readline())
            print("Archivo en la línea 2: ", arxiu.readline())

            print("--------------------------------------")
            print("Todas las líneas del archivo:")
            arxiu.seek(0)#Et permet moure les linies i en aquest cas t'asegures que esta en la posicio 0
            print(arxiu.read())


            print("\n--------------------------------------")

            print("Extraer todas las líneas del archivo en una lista:")
            arxiu.seek(0)
            data = arxiu.readlines()
            print(data)
    except FileNotFoundError as e:
        pass

mostra()