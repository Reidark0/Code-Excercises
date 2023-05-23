cidade01 = {'populacao': 15, 'praia': False, 'regiao': 'Centro-Oeste', 'genticilio': 'Candango'}
cidade02 = {'populacao': 62, 'praia': True, 'regiao': 'Nordeste', 'genticilio': 'Potiguar'}
cidade03 = {'populacao': 2500000, 'praia': True, 'regiao': 'Nordeste', 'genticilio': 'Jampense'}

dictCidades = {'Brasilia - DF': cidade01,
                'Natal - RN': cidade02, 
                'Jampa - PR': cidade03}

print(dictCidades['Brasilia - DF']['regiao'])