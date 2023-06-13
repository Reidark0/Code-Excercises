'Você está com febre. Tome um remédio e repouse'
'Você está com febre. Tome umm remédio, procure um médico'
'Nada de febre'

def temperatura():
    print('Bem vindo ao Programa de temperatura!')
    resposta = ''
    while resposta != 'sair':
        print('Digite qual é a sua temperatura ou sair para encerrar.')
        resposta = input()
        if resposta == 'sair':
            print('Encerrando o programa.')
            break
        elif float(resposta) >= 38 and float(resposta)  < 39:
            print('Você está com febre. Tome um remédio e repouse')
        elif float(resposta) >= 39:
            print('Você está com febre. Tome umm remédio, procure um médico')
        else:
            print('Nada de febre')



temperatura()