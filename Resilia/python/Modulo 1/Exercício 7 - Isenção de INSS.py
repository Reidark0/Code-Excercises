'''
O que é para fazer:

Escreva um programa em Python que exiba o desconto do INSS segundo seu salário.
Por exemplo, se o usuário possuir salário inferior ou igual a R$: 600,00 ele será isento,
em caso de maior que R$: 600,00 e menor ou igual a R$:1.200,00, o desconto é de 20%; 
em caso de Maior que R$: 1.200,00 e menor ou igual a R$: 2.000,00, o desconto é de 25%; 
e em caso de maior que R$: 2.000,00, o desconto é de 30%.

Como Fazer:

Crie uma variável para receber o salário do usuário;
Crie uma condição para fazer as verificações necessárias;
Dentro das verificações, crie a variável que vai armazenar o cálculo do desconto;
Imprima o valor do desconto para o usuário.
'''

salario = float(input('Digite o seu salário: '))
if salario <= 600:
    print(f'Você é isento do INSS, seu salário liquido é {salario}')
elif salario >600 and salario <= 1200:
    desconto = salario * 0.8
    print(f'Você será descontado 20% do salário para contribuir para o INSS, seu salario liquido é {desconto}')
elif salario >1200 and salario <= 2000:
    desconto = salario * 0.75
    print(f'Você será descontado 25% do salário para contribuir para o INSS, seu salario liquido é {desconto}')
elif salario >2000:
    desconto = salario * 0.7
    print(f'Você será descontado 30% do salário para contribuir para o INSS, seu salario liquido é {desconto}')
    