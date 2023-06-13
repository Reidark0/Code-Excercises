class Gato():
    nome = ''
    dataNascimento = ''
    raca = ''
    
    def miar(self, nome):
        print(f'O gato {nome} miou!')
    
    def comer(self, nome):
        print('o Gato', nome, 'comeu!')


gato01 = Gato()
gato01.nome = 'alfredo'
gato01.dataNascimento = '25/05/2023'
gato01.raca = 'siamês'

gato02 = Gato()
gato02.nome = 'Bahuan'
gato02.dataNascimento = '27/12/1997'
gato02.raca = 'humano'

gato01.comer(gato01.nome)
gato02.miar(gato02.nome)