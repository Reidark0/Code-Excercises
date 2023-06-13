# Manipulação de tuplas.
# 
# Crie uma tupla com 5 elementos e realize as seguintes operações: 
# 1-Imprima na tela o tamanho da tupla;
# 2-Crie uma nova tupla que contenha os elementos da tupla original em ordem reversa;
# 3-Imprima na tela os elementos da nova tupla separados por ""-"".

tupla = ('1', '3', '2', '5', '4')

print(len(tupla))
tupla2 = tupla[::-1]
print('-'.join(tupla2))