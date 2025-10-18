x = int(input("Escoge un número: "))  # Conversión de entrada a entero
if x < 0:
    print(f"{x} Menor que 0")
elif x > 0:
    print(f"{x} Mayor que 0")
elif x == 0:
    print(f"{x} Igual que 0")

if x != 0:
    print(f"{x} Diferente que 0") 
# Una vez un se encuentra la condicion correcta, deja de ejecutar


y = int(input("Escoge un número: "))  # Conversión de entrada a entero
if y < 5 & y > 0:
    print(f"{y}, Menor que 5, Suspendido")
elif y >= 5 & y < 7:
    print(f"{y}, Entre 5 y <7 Aprovado")
elif y >= 7 & y < 10:
    print(f"{y}, 7+ Excelente")
else:
    print(f"{y}, Error, {y} fuera de rango")
    