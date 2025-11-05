def senseNegatius(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = -list[i]
    return list

llista1=[45, -6, 0, -32, 23, 9]

llista2=senseNegatius(llista1)
print(llista2)

def inversa(list):
    llista3 = []
    for i in range(len(list)):
        llista3.append(list[i * -1 - 1])
    return llista3

llista4=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
llista3=inversa(llista4)
print(llista3)
