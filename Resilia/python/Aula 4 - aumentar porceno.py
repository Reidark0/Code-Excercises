valorInicial = float(input("Valor inicial: R$ "))
porcentagem = int(input("Porcentagem do aumento:  "))
valorFinal = valorInicial * (porcentagem/100 + 1)
print(f"O valor final é: {valorFinal}")