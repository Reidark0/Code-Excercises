# Gráfico de Barras com Seaborn
# 
# O que é para fazer:
# Crie um gráfico de barras utilizando a biblioteca Seaborn para visualizar a quantidade de vendas por mês.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

meses = [1,2,3,4,5,6]
vendas = [7,5,2,4,4,3]
data = {'Meses': meses, 'Vendas': vendas}
df = pd.DataFrame(data)

sns.barplot(x='Meses', y='Vendas', data=df)
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()