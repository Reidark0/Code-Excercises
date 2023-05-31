class Fatura():
    def __init__(self, categoria):
        self.categoria = categoria
class Pessoa():
    def __init__(self, nome, fatura):
        self.nome = nome
        self.fatura = fatura
class Casa():
    def __init__(self, cor, pessoa):
        self.cor = cor
        self.pessoa = ''

agua = Fatura('vital')
pai = Pessoa('Rafael', '')
mae = Pessoa('Bianca', agua)
apartamento = Casa('amarela', mae)
