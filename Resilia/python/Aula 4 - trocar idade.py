print('teste 1')
minhaIdade = 25
idadeColega = 40
print(f"minha idade é {minhaIdade}, e a idade do colega é {idadeColega}")
minhaIdade, idadeColega = idadeColega, minhaIdade
print(f"minha idade é {minhaIdade}, e a idade do colega é {idadeColega}")
print("Teste 2")
minhaIdade2 = 22
idadeColega2 = 34
print(f"minha idade é {minhaIdade2}, e a idade do colega é {idadeColega2}")
troca = minhaIdade2
minhaIdade2 = idadeColega2
idadeColega2 = troca
print(f"minha idade é {minhaIdade2}, e a idade do colega é {idadeColega2}")
