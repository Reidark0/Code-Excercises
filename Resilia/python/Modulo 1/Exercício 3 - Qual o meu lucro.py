'''
O que é para fazer:

Um lojista comorou diversos produtos para sua loja e deseja revendê-lo com margem de 
lucro diferente dependendo do valor; por exemplo, ele deseja obter lucro de 45% caso o 
produto custe menos que R$ 20,00. Porém, caso o produto custe mais que isso, o lucro 
1deve ser de 30%. Escreva um programa em Python que ajude esse lojista.

Como Fazer:

Crie uma variável para receber o valor do produto;
Crie uma condição para verificar a condição solicitada;
Dentro da condição, realize o cálculo necessário.
Imprima as informações para o usuário.
'''

valor=float(input("valor do produto: R$"))
if valor >=20:
    print("o valor de venda com lucro de 30% é R${:.2f}".format(valor*1.30))
elif valor < 20:
    print("o valor de venda com lucro de 45% é R${:.2f}".format(valor*1.45))
