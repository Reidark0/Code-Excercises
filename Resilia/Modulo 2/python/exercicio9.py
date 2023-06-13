# Cálculo de área de retângulo.
# 
# Crie uma classe Retangulo que tenha os atributos base e altura e os métodos area e perimetro. 
# Em seguida, crie um objeto da classe Retangulo, leia os valores de base e altura 
# desse objeto do usuário e exiba na tela a área e o perímetro do retangulo.

class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def perimetro(self):
        return (self.base + self.altura) * 2
    
    def area(self):
        return self.base * self.altura
    
retangulo = Retangulo(int(input('altura: ')), int(input('base: ')))
print(retangulo.altura, retangulo.base, retangulo.perimetro())