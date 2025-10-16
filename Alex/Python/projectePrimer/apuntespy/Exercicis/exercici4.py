numeros = []
print('Llista 1-5')
for i in range(5):
    numeros.append(i+1)
for n in numeros:
    print(n, end='')
print()
print('Afegeix el numero 6')
numeros.insert(5,6)


for n in numeros:
    print(n, end='')
print('')
if 3 in numeros:numeros.remove(3)

for n in numeros:
    print(n, end='')
print('')
if len(numeros)<3:numeros.pop(3)

for n in numeros:
    print(n, end='')
print('')
text = "-".join(map(str,numeros))
print(text)
      




