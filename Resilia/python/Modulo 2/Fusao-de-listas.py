lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]
lista3 = [numeros for numeros in range(len(lista1)) for numeros in [lista1[numeros], lista2[numeros]]]
print(lista3)
lista3 = []
for i in range(len(lista2)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)
