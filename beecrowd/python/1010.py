'''
Simple Calculate
'''

produto1, qnt1, preco1 = input().split()
produto2, qnt2, preco2 = input().split()
print(f'VALOR A PAGAR: R$ {(int(qnt1)* float(preco1)) + (int(qnt2) * float(preco2)):.2F}')