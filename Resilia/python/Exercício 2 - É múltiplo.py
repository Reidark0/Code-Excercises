'''
O que é para fazer:

Escreva um programa que informe ao usuário se um número é ou não um múltiplo de 5.

Como Fazer:

Crie uma variável que armazene o número digitado pelo usuário;
Faça a verificação com uma condicional realizando o cálculo necessário;
Coloque as saídas de impressão dentro dessa condição.
'''

Numero = float(input("Digite um numero para saber se ele é multiplo de 5"))
if Numero % 5 == 0:
    print("É multiplo de 5")
else:
    print("Não é multiplo de 5")