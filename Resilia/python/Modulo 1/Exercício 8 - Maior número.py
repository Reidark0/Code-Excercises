'''
O que é para fazer:

Defina uma função que usa três números como argumentos e retorna o maior deles.

Como Fazer:

Crie uma função para realizar o cálculo necessário;
Dentro da função, realize condições para verificação;
Chame a função e imprima o resultado.
'''

def maior(a,b,c):
    if a == b and b == c and c == a:
        return ('São todos iguais')
    elif a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

a = float (input('Primeiro número: '))
b = float (input('Segundo número: '))
c = float (input('Terceiro número: '))
print(f'o maior número é: {maior(a, b , c)}')
