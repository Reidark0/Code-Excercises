'''
O que é para fazer:

Escreva um programa que encontrará todos esses números que são divisíveis por 7, 
mas não são um múltiplo de 5, entre 2000 e 3200 (ambos incluídos).

Como Fazer:

Crie uma lista para armazenar os números;
Crie um laço para percorrer o processo no intervalo solicitado;
Crie uma condição para verificar o que foi solicitado;
Adicione os resultados na lista criada anteriormente;
Imprima os valores para o usuário.
'''

lista = []
for a in range(2000,3201):
    if a % 7 == 0 and a % 5 != 0:
        lista.append(a)
print(lista)