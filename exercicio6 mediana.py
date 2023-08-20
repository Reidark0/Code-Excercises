# Mediana de uma lista
# 
# O que é para fazer:
# Crie uma função que receba uma lista de números e retorne a mediana dos valores.

def calcular_mediana (lista):
    lista.sort()
    mediana = len(lista)/2
    if len(lista) % 2 == 0:
        mediana = int(mediana)
        return (lista[mediana] + lista[mediana - 1]) / 2
    else:
        mediana = mediana - 0.5
        mediana = int(mediana)
        return lista[mediana]
        
    
a = [1,2,3,4,5,6,7,8,9]
print(len(a))
print(calcular_mediana(a))