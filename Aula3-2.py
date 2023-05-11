# Retirar os numeros impar e ordenar do menor pro maior
lista = [1, 3, 76, 12, 45, 864, 98, 23, 87, 24, 80, 456, 152, 43, 900]

while lista:
    for i in range(len(lista)):
        print(lista)
        if lista[i] % 2 == 1:
            print('deletar', lista[i])
            lista.pop(i)
            break

print(lista)
