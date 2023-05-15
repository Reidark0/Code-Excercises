def criar(x):
    lista = []
    for i in range(x):
        lista.append(i)
    return lista

def remover(lista):
    return lista.pop()

def tamanhoPilha(lista):
    return len(lista)

def verificar(lista):
    if tamanhoPilha(lista) == 0:
        print('Lista vazia')
    else:
        print(f'Lista com {len(lista)} itens')


lista = criar(10)
print(lista)
verificar(lista)


for i in range(len(lista)):
    remover(lista)

print(lista)
verificar(lista)
