pizzas = ['calabresa', 'frango', 'marquerita']
pizzas_friends = pizzas[:]

pizzas.append('mineira')
pizzas_friends.append('portuguesa')

print(f'as minhas pizzas favoritas são: {", ".join(pizzas)}')
print(f'as pizzas favoritas do meu amigo são: {", ".join(pizzas_friends)}')
