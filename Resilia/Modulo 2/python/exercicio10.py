# Cadastro de alunos.
# 
# Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. 
# Em seguida, crie um objeto da classe Aluno, leia os valores de nome, idade e matrícula desse objeto do usuário 
# e exiba na tela os dados do aluno cadastrado.

class Aluno():
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
    def get_all(self):
        return (self.nome, self.idade, self.matricula)

aluno = Aluno(input(), int(input()), int(input()))

print(aluno.get_all())
