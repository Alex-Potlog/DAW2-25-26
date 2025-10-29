fitxer = open('nom_fitxer',"r") #r por defecto,Leer el archivo
fitxer = open('nom_fitxer',"w") #write, crea si no hay, al escribir, sobreescribe el documento
fitxer = open('nom_fitxer',"a") #append, cuando escribe añade al documento, Mejor este
fitxer = open('nom_fitxer',"x") #crea archivo pero si existe da error
fitxer = open('nom_fitxer',"rb") #binario
fitxer = open('nom_fitxer',"rt") #texto, por defecto

with open('nom_fitxer','wt') as f:#with cierra el documento al acabar
    f.read()

fitxer.read() #lee todo el documento
fitxer.read(5) #lee los primeros 5 CARACTERES
fitxer.readline(4) #lee la linea 4

fitxer.write("a") #añade al final del documento
fitxer.writelines()#puedes usar una lista de strings para añadir lineas (una por objeto), si no usa write con un \n al final de cada linea, es lo mismo

fitxer.close() #Pues eso

