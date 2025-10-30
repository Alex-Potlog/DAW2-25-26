# 1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. 
# Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

#file=open('exemple.txt', 'r')

def mostra(fitxer):
    try:
        with open(fitxer, 'r') as file:
            print(file.readlines())
    except FileNotFoundError:
        print("Fitxer no trobat")
    finally:
        try:
            file.close()
        except:
            pass

mostra('exemple.txt')
# 2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer 
# al primer fitxer. Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.
def concatena(fitxer1, fitxer2):
    try:
        with open(fitxer2, 'r') as file2:
            content=file2.read()
        with open(fitxer1, 'a') as file:
            file.write(content)
        
        print(f"El contingut del '{file2.name}' afegit a '{file.name}' correctament")

        with open(fitxer1, 'r') as file:
            print(file.readlines())
            
    except FileNotFoundError:
        print("Fitxer(s) no trobat")
    finally:
        try:
            file.close()
            file2.close()
        except:
            pass

concatena('exemple.txt', 'exemple2.txt')

# 3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, 
# el contingut original del fitxer no s'ha d'esborrar.

def afegir (fitxer, llista):
    try:
        with open(fitxer, 'a') as file:
            for element in llista:
                file.write(element+"\n")
        
        with open(fitxer, 'r') as file:
            print(file.readlines())
    except FileNotFoundError:
        print("Fitxer no trobat")
    except Exception:
        print("Hi ha hagut un error")
    finally:
        try:
            file.close()
        except:
            pass

llista= ["Rosa", "Margarita", "Girasol", "Orquídia"]

afegir('exemple2.txt', llista)

# 4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició 
# és incorrecta, ha de mostrar un missatge informatiu.

def escriuPos (fitxer, frase, posicio):
    try:
        with open(fitxer, 'r+') as file:
            file.seek(posicio) #En aquest cas es mou a la posicio indicada
            file.write(frase)
        
        print(f"El contingut s'ha afegit a correctament")

        with open(fitxer, 'r') as file:
            print(file.readline())
            

    except Exception:
        print("Fitxer no trobat i/o hi ha hagut un error")
    finally:
        try:
            file.close()
        except:
            pass

frase='Bon dia a la vila del pingui'
posicio=5

escriuPos ('exemple.txt', frase, posicio)
#-------------------------------------------------------------
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