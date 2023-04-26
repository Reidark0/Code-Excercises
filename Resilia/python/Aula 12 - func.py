def dirigirOuBeber(idade):
    if idade >= 18:
        print('Já pode dirigir ou beber.')
    else:
        print('Não pode dirigir nem beber.')


idade = int(input('Qual é a sua idade? '))
dirigirOuBeber(idade)