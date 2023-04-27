'''
Uma ONG que trabalha com preservação ambiental precisa realizar uma pesquisa
com o público para entender qual a percepção deles em relação às ações que os
prefeitos de cada cidade estão realizando sobre esse assunto.
Para ajudar a verificar quantas pessoas precisam ser entrevistadas em cada uma das
capitais do Brasil e ajudar a pesquisa a ter uma boa amostragem, vamos montar um
código na linha de comando que faça esse cálculo. Será informado a população
da cidade e a margem de erro esperada.

■ O código precisa exibir a quantidade de pessoas que a ONG vai precisar
entrevistar;
■ Visualizar uma calculadora similar e informações relativas a como realizar o
cálculo que irá ajudar a testar se seu código está devolvendo os resultados
corretamente;
■ A entrega deverá ser realizada em um único arquivo .py (que pode ser enviado
como texto em alguma plataforma (Google Docs) ou então como arquivo
compartilhado (Google Drive, One Drive, etc).
'''

def elev2(a):
    b = a * a
    return b

def previsao(a): 
    b = a * (1 - a)
    return b


popCidade = int(input('Qual a população da cidade? '))
margErro = int(input('Qual a margem de erro da pesquisa em %? '))
z = 1.96
e = margErro/100
if popCidade < 100000:
    result = (popCidade * elev2(z) * previsao(0.5)) / ((popCidade - 1) * elev2(e) + elev2(z) * previsao(0.5))
elif popCidade > 100000:
    result = (elev2(z) * previsao(0.5)) / elev2(e)
print(f"O número mínimo de entrevistados necessário é {round(result)}")