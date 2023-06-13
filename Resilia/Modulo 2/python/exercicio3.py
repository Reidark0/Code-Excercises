# Soma de valores em uma lista. 
# 
# Crie uma lista com 5 números inteiros de sua escolha e calcule a soma desses valores. 
# Imprima o resultado da soma na tela.

lista = [1, 2, 3, 4, 5]
soma = 0

for i in lista:
    soma += i

print(soma)

print(sum(lista))
