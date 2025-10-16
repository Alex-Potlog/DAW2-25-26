list1 =  ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for i in list1:
    print(i, end=' ')

print()

for i in range(len(list1)):
    print(list1[i * -1 - 1], end=' ')


