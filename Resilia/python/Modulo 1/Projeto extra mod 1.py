# Uma ONG que trabalha com preservação ambiental precisa realizar uma pesquisa
# com o público para entender qual a percepção deles em relação às ações que os
# prefeitos de cada cidade estão realizando sobre esse assunto.
# Para ajudar a verificar quantas pessoas precisam ser entrevistadas em cada uma das
# capitais do Brasil e ajudar a pesquisa a ter uma boa amostragem, vamos montar um
# código na linha de comando que faça esse cálculo. Será informado a população
# da cidade e a margem de erro esperada.

# ■ O código precisa exibir a quantidade de pessoas que a ONG vai precisar
# entrevistar;
# ■ Visualizar uma calculadora similar e informações relativas a como realizar o
# cálculo que irá ajudar a testar se seu código está devolvendo os resultados
# corretamente;
# ■ A entrega deverá ser realizada em um único arquivo .py (que pode ser enviado
# como texto em alguma plataforma (Google Docs) ou então como arquivo
# compartilhado (Google Drive, One Drive, etc).

def quadrado(num):      # função de elevar o numero ao quadrado
    return num * num

def previsao(chanceEsperada):       # A chance esperada inicial é 50%, ou seja, 50% de ser ou não.
    return chanceEsperada * (1-chanceEsperada)

def popPequena(popCidade, margErro, zScore):    # Calculo da quantidade de entrevistados em uma população pequena (< 100,000)
    return (popCidade*quadrado(zScore)*previsao(0.5)) / ((popCidade-1)*quadrado(margErro) + quadrado(zScore)*previsao(0.5))

def  popGrande(margErro, zScore):       # Calculo da quantidade de entrevistados me populações grandes
    return (quadrado(zScore)*previsao(0.5)) / quadrado(margErro)


desvioPadraoDic = {1 : 1.282,
                   2 : 1.440,
                   3 : 1.645,       # Desvio padrão em relação ao grau de confiança selecionado
                   4 : 1.960,
                   5 : 2.576,
                   6 : 3.291}
popCidade = int(input('Qual a população da cidade? '))
margErro = int(input('Qual a margem de erro da pesquisa em %? '))
grauConfiaca = int(input(f'Qual o Grau de confiaça que você precisa(recomendamos usar 95%)?\n'
                         f'1 - 80%\n'
                         f'2 - 85%\n'
                         f'3 - 90%\n'
                         f'4 - 95%\n'
                         f'5 - 99%\n'
                         f'6 - 99.9%\n'))
zScore = desvioPadraoDic[grauConfiaca]
margErro = margErro/100                # Trasnformar a margem de erro em porcentagem.
if popCidade < 100000:
    result = popPequena(popCidade, margErro, zScore)
elif popCidade > 100000:
    result = popGrande(margErro, zScore)
print(f"O número mínimo de entrevistados necessário é {round(result)}")
