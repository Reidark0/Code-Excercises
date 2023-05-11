import random


def a():
    return random.randint(1,10)
def selecao(entrevistaCorte, teoricoCorte, praticoCorte, softCorte, lista):
    selecionados_e = []
    selecionados_t = []
    selecionados_p = []
    selecionados_final = []
    # e_nota, t_nota, p_nota e s_nota servem para reduzir o tamanho do código.
    for candidato in range(len(lista)): 
        # pega o item da lista, faz um slicing da string, isola a nota e converte em int
        e_nota = lista[candidato]
        if int(e_nota[e_nota.find('e') + 1:e_nota.find('_')]) >= entrevistaCorte:   # Corte da entrevista
            selecionados_e.append(e_nota) 
    for candidato in range(len(selecionados_e)): 
        t_nota = selecionados_e[candidato][selecionados_e[candidato].find('_') +1:]
        if int(t_nota[t_nota.find('t') + 1 : t_nota.find('_')]) >= teoricoCorte:    # Corte do teórico
            selecionados_t.append(selecionados_e[candidato])
    for candidato in range(len(selecionados_t)):
        p_nota = selecionados_t[candidato][selecionados_t[candidato].find('p'):]
        if int(p_nota[p_nota.find('p') + 1:p_nota.find('_')]) >= praticoCorte:      # Corte do prático
            selecionados_p.append(selecionados_t[candidato])
    for candidato in range(len(selecionados_p)):
        s_nota = selecionados_p[candidato][selecionados_p[candidato].find('s') + 1:]
        if int(s_nota) >= softCorte:                                                # Corte do Soft
            selecionados_final.append(selecionados_p[candidato])
    return selecionados_final


candidatos_aleatórios = [] # criar lista de candidatos aleatórios
for i in range(20):
    candidatos_aleatórios.append(f'e{a()}_t{a()}_p{a()}_s{a()}')

print(selecao(7, 7, 7, 7, candidatos_aleatórios))
