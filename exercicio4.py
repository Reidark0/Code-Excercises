# Manipulação de Dataframes
# 
# O que é para fazer:
# Crie um Dataframe com informações de alunos e realize manipulações avançadas.

import pandas as pd

aluno1 = {'Nome':'Rafael', 'Idade':25, 'Area':'Veterinaria', 'Nota': 'MS'}
aluno2 = {'Nome': 'Bianca', 'Idade':22,'Area':'Design','Nota':'SS'}
alunos = pd.DataFrame([aluno1,aluno2])
alunos.query('Nome == Bianca')
