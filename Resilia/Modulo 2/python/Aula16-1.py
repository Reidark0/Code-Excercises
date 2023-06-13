class Funcionario():
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.salarioBase = salarioBase

    def calcularSalario (self):
        print(self.salarioBase)

class FuncionarioPJ(Funcionario):
    pass
class FuncionarioCLT(Funcionario):
    pass




class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcularSalario(self):
        pass


class FuncionarioClt(Funcionario):
    def __init__(self, nome, salario_base, meses_empresa):
        super().__init__(nome, salario_base)
        self.meses_empresa = meses_empresa

    def calcularSalario(self):
        return self.salario_base * (self.meses_empresa / 100)


class FuncionarioPj(Funcionario):
    def __init__(self, nome, salario_base, experiencia):
        super().__init__(nome, salario_base)
        self.experiencia = experiencia

    def calcularSalario(self):
        return self.salario_base * self.experiencia


clt = FuncionarioClt("João", 2000, 12)
pj = FuncionarioPj("Maria", 1500, 2)

print(f"Salário CLT: R$ {clt.calcularSalario()}")
print(f"Salário PJ: R$ {pj.calcularSalario()}")
