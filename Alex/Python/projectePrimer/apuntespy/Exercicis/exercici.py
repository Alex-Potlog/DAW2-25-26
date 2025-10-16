barrufetsAmbDret = int(input("Total de barrufets amb dret a vot la país"))
barrufetsHanVotat = int(input("Total de barrufets que han votat"))
votsAfirmatius = int(input("Total de Vots afirmatius"))
votsNegatius = int(input("Total de Vots Negatius"))

percentatgeParticipacio = barrufetsHanVotat/barrufetsAmbDret*100
percentatgeAfirmatius = votsAfirmatius/barrufetsHanVotat*100
percentatgeNegatius = votsNegatius/barrufetsHanVotat*100
votsBlancs = (barrufetsHanVotat - votsNegatius - votsAfirmatius) 

if percentatgeAfirmatius >percentatgeNegatius:
    print(f"Ha guanyat el SI amb {percentatgeAfirmatius:.2f}")
elif percentatgeAfirmatius<percentatgeNegatius:
    print(f"Ha guanyat el SI amb {percentatgeNegatius:.2f}")
else:
    print(f"Empatat")
print(f"Vots Blancs {votsBlancs}")
