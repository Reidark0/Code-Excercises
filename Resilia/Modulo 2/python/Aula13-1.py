class Fatura():
    def __init__(self):
        self.categoria = ''

class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.fatura = Fatura()
        self.endereco = endereco

class Casa():
    def __init__(self, endereco):
        self.endereco = endereco

endereco = Casa('SHVP rua 4')
rafael = Pessoa('Rafael', endereco)
rafael.fatura.categoria = 'agua'

