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

def elev2(a):
    return a * a

def previsao(a): 
    return a * (1-a)

def popPequena(popCidade, e):
    return (popCidade*elev2(1.96)*previsao(0.5)) / ((popCidade-1)*elev2(e) + elev2(1.96)*previsao(0.5))

def  popGrande(e):
    return (elev2(1.96)*previsao(0.5)) / elev2(e)

# 1.96 é o socre Z de 95% que é a margem de confiança usada comunmente.
# 0.5 é o resultado esperado, usamos 0.5 quando não fazemos ideia do resultado (50% de chance de ser uma coisa ou outra)

popCidade = int(input('Qual a população da cidade? '))
margErro = int(input('Qual a margem de erro da pesquisa em %? '))
e = margErro/100                # Trasnformar a margem de erro em porcentagem.
if popCidade < 100000:
    result = popPequena(popCidade, e)
elif popCidade > 100000:        # Quando a população é muito grande ( += de 100.000 ) podeoms usar a equação simplificada
    result = popGrande(e)
print(f"O número mínimo de entrevistados necessário é {round(result)}")
