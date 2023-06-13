'''
O que é para fazer:

Escreva um programa em Python que some diversos números fornecidos pelo usuário. 
A quantidade de números que serão somados, também deve ser fornecida pelo usuário.

Como Fazer:

Crie uma variável para receber a quantidade de números que serão somados a ser fornecida pelo usuário;
Crie um laço para percorrer a quantidade de vezes que o usuário informarna variável anterior;
Crie as variáveis de número e soma;
Realize o cálculo necessário;
Imprima a informação para o usuário.
'''

quantidadeLoop = int(input("Quantos números você quer somar? "))
i = 0
resposta = 0
while i < quantidadeLoop:
    resposta += float(input("Seu número: "))
    i += 1
print(f"A soma dos seus números é: {resposta}")