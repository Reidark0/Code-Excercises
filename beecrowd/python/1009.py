'''
Salary with Bonus
'''

nome = input()
salario = float(input())
vendas = float(input())
print(f'TOTAL = R$ {salario + (vendas*0.15):.2F}')
