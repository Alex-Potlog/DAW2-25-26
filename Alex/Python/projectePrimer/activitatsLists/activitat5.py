list1 = [45, -6, 0, -32, 23, 9]
listCorrecte = []

for i in range(len(list1)):
    if list1[i] < 0:
        listCorrecte.append((list1[i] * -1))
    else:
        listCorrecte.append(list1[i])

parells = []

for i in range(len(listCorrecte)):
    if (listCorrecte[i] % 2 == 0):
        parells.append(listCorrecte[i])
        
print(parells)