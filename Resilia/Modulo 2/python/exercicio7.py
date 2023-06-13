# Representando um Animal
# 
# Crie uma classe simples em Python para representar um animal. 
# A classe deve ter um atributo "nome" e um método "falar",
# que exibe uma mensagem na tela com o som que o animal faz.

class animal():
    nome = ''
    
    def falar(self, nome):
        print('o', nome, 'falou!')

cachorro = animal()
cachorro.nome = 'cachorro'
cachorro.falar(cachorro.nome)
