# Média de uma lista
# 
# O que é para fazer:
# Crie uma função que receba uma lista de números e retorne a média dos valores.

import pandas as pd
serie = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(serie.mean())


def calcular_media(lista):
    a = 0
    for x in lista:
        a +=x
    return a / len(lista)

nume = [1,2,3,4,5,6,7,8,9,10]
print(calcular_media(nume))
