# Age in Days

dias = int(input())
ano = 0
mes = 0
while dias >= 365:
    dias -= 365
    ano += 1
while dias >= 30:
    dias -= 30
    mes += 1
print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dias, 'dia(s)')