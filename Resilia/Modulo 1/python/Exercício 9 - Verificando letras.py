'''
O que é para fazer:

Escreva uma função que receba uma string e retorne True se for uma vogal e False caso contrário

Como Fazer:

Crie uma função para realizar o cálculo necessário;
Dentro da função, realize condições para verificação;
Chame a função e imprima o resultado.
'''

def vogal (letra):
    if letra in "aeiou":
        return True
    else:
        return False


string = input('Escreva uma letra:')
print(vogal(string))
