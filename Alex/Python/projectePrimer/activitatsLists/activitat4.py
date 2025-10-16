llista =  ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for i in range(len(llista)):
    if (i % 2 == 0) :
        print(llista[i], end=' ')
print()
for i in range(len(llista)):
    if (i % 2 == 1) :
        print(llista[i], end=' ')