# função zip

lista01 = [1, 2, 3, 4, 5]
lista02 = ['a', 'b', 'c', 'd', 'e']
lista03 = ['f', 'g', 'h', 'i', 'j']

for item1, item2, item3 in zip(lista01, lista02, lista03):
    # print(type(item1), type(item2), type(item3))
    pass

#DICIONÁRIO DE DICIONÁRIOS

#vários dicionários


pao01 = {'cor': 'branco', 'consistencia' : 'macio', 'quantidade' : 26}
pao02 = {'cor': 'moreno', 'consistencia' : 'meia-bomba', 'quantidade' : 11}
pao03 = {'cor': 'preto', 'consistencia' : 'duro', 'quantidade' : 4}
pao04 = {'cor': 'vermelho', 'consistencia' : 'macio', 'quantidade' : 2}

dic_paes = {'frances': pao01, 'careca': pao02, 'podre': pao03, 'sangue': pao04}

for x in dic_paes.items():
    print(x)