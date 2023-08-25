# Moda de uma lista
# 
# O que é para fazer
# Crie uma função que receba uma lista de números e retorne a moda dos valores.

def calcular_moda(lista):
    moda = dict()
    for x in lista:
        moda[x] = lista.count(x)
    keys = list(moda.keys())
    values = list(moda.values())
    rst = values.index(max(values))
    return keys[rst]


a = [1,2,3,3,3,6,6,6,6,6,6]
print(calcular_moda(a))
