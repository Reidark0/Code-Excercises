# Gráfico de Linha com Matplotlib
# 
# O que é para fazer:
# Crie um gráfico de linha utilizando a biblioteca Matplotlib para visualizar a variação de temperatura ao longo de uma semana.

import matplotlib.pyplot as plt

temp = [17,19,20,20,23,23,17,21,19,23]
dias = [1,2,3,4,5,6,7,8,9,10]

plt.plot(dias, temp)
plt.xlabel('Dia mês')
plt.ylabel('Temperatura')
plt.show()