lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]

lista3 = [x for i in range(len(lista2)) for x in [lista1[i], lista2[i]]]

print(lista3)
