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

            arxiu.close()
    except FileNotFoundError as e:
        raise FileNotFoundError("No es poden introduir quest tipus de fitxers",e)

# mostra()

def concatena(fitxer1,fitxer2):
    contingut=""
    contingut2=""
    try:
        with open(fitxer1, "r") as arxiu:
            contingut=arxiu.read()
            arxiu.close()
        
        with open(fitxer2, "r") as arxiu2:
                contingut2 = arxiu2.read()
                arxiu2.close()
        
        with open(fitxer2,"w") as escritura:#El w+ es per escritura i lectura, pero elimina el contingut
            contingut_total = contingut + contingut2
            escritura.write(contingut_total)
            escritura.close()

        with open(fitxer2,"r") as lectura:
            infof = lectura.read()
            print(infof)
            lectura.close()


    except FileNotFoundError as e:
        raise FileNotFoundError("Error en el fitxer")
    
# concatena("exemple.txt","exemple2.txt")

def afegir(llista):
    contingut=""
    try:
        with open("exemple.txt","r") as lectura:
            contingut=lectura.read()
            lectura.close()

        with open("exemple.txt","a") as escritura:
            for element in llista:
                contingut = contingut+"\n"+element
            escritura.write(contingut)
            escritura.close()

    except FileNotFoundError as e:
        pass

# text=""
# llista=[]
# while text !="$":
#     text = str(input("Introdueix un valor dins a la$"))
#     if text !="$":
#         llista.append(text)
# afegir(llista)

def escriuPos():
    despres="assas"
    contingut="to"
    llista_inicial=[]
    llista_final=[]
    try:
        with open("exemple.txt","r") as lectura:
            llista_inicial=lectura.readlines()#Retorna una llista
            lectura.close()
        # fitxer1 = open("exemple.txt","+a") al fitxer1 pots llegir i fer append


        for element in llista_inicial:
            if despres in element:
                llista_final.append(contingut)
            llista_final.append(element)

        with open("exemple.txt","w+") as escriptura:
            for element in llista_final:
                escriptura.write(element)
                escriptura.close()

    except FileNotFoundError as e:
        raise FileNotFoundError("No ha trobat el fitxer")

escriuPos()