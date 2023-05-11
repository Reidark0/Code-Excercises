# multiplicar duas listas r colocar o resultado em outra lista

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [11,12,13,14,15,16,17,18,19,20]
lista_final = []
for i in range(len(lista1)):
    lista_final.append(lista1[i] * lista2[i])
print(lista_final)

# Gabartito seria:
lista_final = [0] * 10
for i in range(len(lista1)):
    lista_final[i] = lista1[i] * lista2[i]
print(lista_final)
