'''
O que é para fazer:

Escreva uma programa em Python que peça a quantidade de pacientes e 
calcule o IMC a partir do nome, peso e altura para cada um deles.

Como Fazer:

Crie uma variável que vai armazenar o número de pacientes;
Crie um for para percorrer a quantidade de pacientes;
Crie variáveis para armazenar nome, altura e peso;
Crie uma variável para calcular o IMC e faça o cálculo necessário;
Imprima os dados na tela.
'''

tabela = {}
numero = int(input("Número de pacientes: "))
for paciente in range(1,numero + 1):
    nome = input(f'Digite o nome do Paciente {paciente}: ')
    altura = float(input(f"Digite a altura do Paciente {paciente} em metros: "))
    peso = float(input(f'Digite o peso do paciente {paciente} em kg: '))
    imc = peso / (altura ** 2)
    tabela[nome] = imc
for i in tabela:
    print(f'O IMC do {i} é: {tabela[i]}')
