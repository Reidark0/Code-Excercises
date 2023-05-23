dicionario = {'print': 'imprimir',
              'git': 'versionamento',
              'list': 'listas',
              'if':'condição',
              'loop':'repetição'}

print(dicionario)

dicionario.pop('print')
del dicionario['git']
dicionario.popitem()

print(dicionario)

dicionario.clear()

print(dicionario)

dicionario['print'] = 'imprimir'
dicionario.update({'git':'versionamento'})

for chave, valor in dicionario.items():
    print(f'chave {chave} e o valor {valor}')
    