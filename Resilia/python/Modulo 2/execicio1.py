# Fila de espera.
# 
# Crie uma fila de espera com os nomes de cinco pessoas e execute as seguintes operações: 
# 1-Imprima na tela a fila atual. 
# 2-Remova o primeiro elemento da fila e imprima na tela a fila atualizada. 
# 3-Adicione mais dois nomes à fila e imprima na tela a fila atualizada.

fila = ['Rafael', 'Will', 'Rafa', 'Vic', 'Esli']
print(fila)
fila.pop(0)
print(fila)
fila.append('Luciana')
fila.append('Daniel')
print(fila)