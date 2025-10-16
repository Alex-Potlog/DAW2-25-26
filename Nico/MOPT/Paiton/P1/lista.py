lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#afegir
lista.append(11)
#afegirvarios
lista.extend([12, 13, 14])
#eliminar
lista.remove(1)
#mostrar
print(lista)
#mostrarposX
print(lista[0])
#mostrarultim
print(lista[-1])
#mostrarlongitud
print(len(lista))
#mostrar els 4 mes grans
print(sorted(lista, reverse=True)[:4])
#afegirposX
lista.insert(0, 0) 
print(lista)
#eliminarposX
del lista[0]
print(lista)
#eliminarultim
lista.pop()
print(lista)
#eliminarultimvarios
lista = lista[:-3]
print(lista)
#eliminarposXvarios
del lista[0:2]
print(lista)

