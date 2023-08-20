# Gráfico de Dispersão com Matplotlib
# 
# O que é para fazer:
# Crie um gráfico de dispersão utilizando a biblioteca Matplotlib para visualizar a relação entre duas variáveis: altura e peso.

import matplotlib.pyplot as plt


altura = [160,171,175,177,156,180]
peso = [80,120,75,74,66,150]

plt.scatter(altura, peso)
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.show()