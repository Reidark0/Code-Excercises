class pessoa():
    idade = 45  
    cidade = 'São Paulo'
    estado = 'SP'
    salario = 3000
    escolaridade = 'Ensino Médio'
    def imprimirDados(self, idade, cidade, estado, salario, escolaridade):
        print(idade, ',', cidade, ',', estado, ',', salario, ',', escolaridade)

exemplo = pessoa()
exemplo.imprimirDados(exemplo.idade, exemplo.cidade, exemplo.estado, exemplo.salario, exemplo.escolaridade)