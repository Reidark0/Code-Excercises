'''
O que é para fazer:

Escreva um programa que possa calcular o fatorial de um determinado número. 
Os resultados devem ser impressos em uma sequência separada por vírgulas em uma única linha. 
Suponha que a seguinte entrada é fornecida para o programa: 8 Em seguida, a saída deve ser: 40320

Como Fazer:

Crie uma função para realizar o cálculo necessário;
Fora da função, crie uma variável para receber o número do usuário;
Chame a função e imprima o resultado.
'''

def conta(fatorial):
    resultado = 1
    if fatorial > 0:
        for numeros in range (1,fatorial + 1):
            resultado *= numeros
        print(resultado)
    else:
        return print('Só numeros naturais (inteiros e positivos)')


fatorial = int(input('Fatorial de quanto? '))
conta(fatorial)
