barrufetsAmbDret = int(input("Introdueix el nombre de barrufets amb dret a vot: "))
barrufetsVotants = int(input("Introdueix el nombre de barrufets que han votat: "))
votsAfirmatius = int(input("Introdueix el nombre de vots afirmatius: "))
votsNegatius = int(input("Introdueix el nombre de vots negatius: "))

#% de participacio
participacio = (barrufetsVotants / barrufetsAmbDret) * 100
print(f"El % de participacio es {participacio:.2f}%")
#% de vots afirmatius
percentatgeAfirmatiu = (votsAfirmatius / barrufetsVotants) * 100
print(f"El % de vots afirmatius es {percentatgeAfirmatiu:.2f}%")
#% de vots negatius
percentatgeNegatiu = (votsNegatius / barrufetsVotants) * 100
print(f"El % de vots negatius es {percentatgeNegatiu:.2f}%")
#% de vots en blanc
print(f"El % de vots en blanc es {100-participacio:.2f}%")

#resultat votacio
if percentatgeAfirmatiu > 50:
    print("Ha guanyat el SI")
elif percentatgeNegatiu > 50:
    print("Ha guanyat el NO")
else:
    print("La votacio es un empat")