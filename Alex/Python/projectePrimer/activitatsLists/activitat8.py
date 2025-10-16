numLlista = 0
while numLlista < 1 or numLlista > 10:
    numLlista = int(input("Passa un num del 1 al 10: "))
    if numLlista < 1 or numLlista > 10:
        print("Torna a intentar!")
        
for i in range(10):
    print(numLlista * (i+1), end=' ')