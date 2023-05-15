def criar(x):
    lista = []
    for i in range(x):
        lista.append(i)
    return lista

def remover(lista):
    return lista.pop(0)

def verificar(lista):
    if len(lista) == 0:
        print('Lista vazia')
    else:
        print(f'Lista com {len(lista)} itens')


lista = criar(10)

verificar(lista)
print(lista)

for i in range(len(lista)):
    remover(lista)

print(lista)
verificar(lista)
