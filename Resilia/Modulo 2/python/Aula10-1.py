class Cachorro():
    nome = 'Safira'
    idade = '5'
    raca = 'Husky'
    
    def latir(self, nome):
        print(f'O gato {nome} latiu!')
    
    def comer(self, nome):
        print('o Gato', nome, 'comeu!')


cao = Cachorro()
cao.latir(cao.nome)