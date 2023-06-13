class Lampada():
    cor = 'amarela'
    acesa = False

    def acender(self):
        if self.acesa == False:
            self.acesa = True

lampada = Lampada()
print(lampada.acesa)
lampada.acender()
print(lampada.acesa)


class Carro():
    cor = 'amarela'
    def __init__(self, rodas, capacidadeDeTanque, motor):
        self.rodas = rodas
        self.capacidadeDeTanque = capacidadeDeTanque
        self.motor = motor

    def get_cor(self):              # Getter => colocar o nome como:
        return self.cor             #           get_nome da variavel    
    def get_rodas(self):  
        return self.rodas
    
    def set_cor(self, novaCor):     # Setter => mesma regra pro nome
        self.cor = novaCor
    
aneli = Carro(4, 50, 5.0)
arroz = Carro(2, 15, 1.0)
lixo = Carro(0, 0, 0.0)
lista = [aneli, arroz, lixo]
for i in lista:
    print(i.get_cor())
    print(i.get_rodas())
print(aneli.cor)
aneli.set_cor('Vermelho')
print(aneli.cor)
