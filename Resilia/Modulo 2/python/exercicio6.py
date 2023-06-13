# Fila de espera
# USANDO CLASSES
# 
# Crie uma fila de espera com os nomes de cinco pessoas e execute as seguintes operações: 
# 1-Imprima na tela a fila atual
# 2-Remova o primeiro elemento da fila e imprima na tela a fila atualizada
# 3-Adicione mais dois nomes à fila e imprima na tela a fila atualizada.

class coisa():
    lista = []

    def tirar(self, lista):
        lista.pop(0)
        print(lista)
    def colocar(self, lista):
        lista.append('Aaron')
        lista.append('Daniel')
        print(lista)


exemplo = coisa()
exemplo.lista = ['Rafael', 'Will', 'Pedro', 'Lucas', 'Jaq']
print(exemplo.lista)
exemplo.tirar(exemplo.lista)
exemplo.colocar(exemplo.lista)
