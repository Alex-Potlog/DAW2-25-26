# Al país dels Barrufets volen fer un referèndum.
totalDretVot = int (input ("Introdueix el total de Barrufets amb dret a vot: ")) #Nombre de Barrufet que tenen dret a vot
totalVots = int (input ("Introdueix el total de Barrufets que han votat: ")) #Nombre de Barrufet que han vot
votsAfirmatiu= int (input ("Introdueix el total de vots afirmatius: ")) #Nombre de vots que han sigut afirmatius
votsNegatiu= int (input ("Introdueix el total de vots negatius: ")) #Nombre de vots que han sigut negatius

#Càlcul del percentatge de participació que hi ha hagut al referèndum (i mostrat per pantalla)
percentParticipacio = totalVots / totalDretVot*100
print(f"El % de participació ha sigut de [{percentParticipacio}:.2f]")

#Càlcul del percentatge de vots positius que hi ha hagut al referèndum (i mostrat per pantalla)
percentAfirmatius= votsAfirmatiu / totalVots*100
print(f"El % de vots afirmatius ha sigut de [{percentAfirmatius}:.2f]")

#Càlcul del percentatge de vots negatius que hi ha hagut al referèndum (i mostrat per pantalla)
percentNegatius= votsNegatiu / totalVots*100
print(f"El % de vots negatius ha sigut de [{percentNegatius}:.2f]")

#Càlcul del percentatge de vots en blanc i nuls que hi ha hagut al referèndum (i mostrat per pantalla)
percentBlancNuls= (totalVots - votsAfirmatiu - votsNegatiu)/totalVots
print(f"El % de vots en blanc o nuls ha sigut de [{percentBlancNuls}:.2f]")

#Condició: diferenciar si ha guanyat el si, el no o ha sigut empat el referèndum 
# per tal de mostrar el missatge per pantalla que correspongui
if percentAfirmatius>percentNegatius:
    print("Ha guanyat el SI")
elif percentAfirmatius<percentNegatius:
    print("Ha guanyat el NO")
else:
    print("Empat")
