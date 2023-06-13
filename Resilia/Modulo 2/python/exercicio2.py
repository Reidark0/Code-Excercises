# Fusão de listas.
# 
# Crie duas listas de tamanho igual com valores numéricos de sua escolha. 
# Crie uma nova lista que seja a fusão das duas primeiras, 
# de forma que os elementos sejam intercalados. 
# Por fim, imprima a nova lista na tela.

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]

lista3 = [x for i in range(len(lista2)) for x in [lista1[i], lista2[i]]]

print(lista3)
