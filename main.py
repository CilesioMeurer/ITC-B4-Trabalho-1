import random
tamanho_da_mochila = 100 
peso_dos_objetos = [23,31,29,44,53,38,63,85,89,82]
lucro_dos_objetos = [92,57,49,68,60,43,67,84,87,72]
penalidade = 20
tamanho_da_populacao = 6
avaliacoes_total = 35
avaliacoes_atual = 0
tamanho_solucao = len(lucro_dos_objetos)
percentual_mutacao = 2
populacao = []
populacao_futura = []
fitness = [0] * tamanho_da_populacao
fitness_populacao_futura = [0] * (tamanho_da_populacao + 1)
melhor_fitness = []
media_fitness = []
pior_fitness = []
melhor_solucao = 0
pior_solucao = 0

for i in range (tamanho_da_populacao):
    populacao.append([0] * tamanho_solucao)
    populacao_futura.append([0] * tamanho_solucao)
populacao_futura.append([0] * tamanho_solucao)


def objetivo(solucao):
    fitness = 0
    peso = 0
    for i in range(len(solucao)):
        fitness = fitness + (solucao[i] * lucro_dos_objetos[i])
        peso = peso + (solucao[i] * peso_dos_objetos[i])

    if (peso > tamanho_da_mochila):
        fitness = fitness - penalidade

    return fitness

def avaliar_solucao(indice):
    fitness[indice] = objetivo(populacao[indice])

def avaliar_populacao():
    for i in range(tamanho_da_populacao):
        avaliar_solucao(i)

def identifica_melhor_solucao():
    melhor_solucao = 0
    for i in range(tamanho_da_populacao):
        if fitness[melhor_solucao] < fitness[i]:
            melhor_solucao = i
    return melhor_solucao

def mutacao(indice):
    for i in range(tamanho_solucao):
        if random.randint(0, 100) <= percentual_mutacao:
            if populacao[indice][i] == 0:
                populacao_futura[indice][i] = 1
            else:
                populacao_futura[indice][i] = 0
        else:
            populacao_futura[indice][i] = populacao[indice][i]

def elitismo():
    melhor_solucao = identifica_melhor_solucao()
    populacao_futura[tamanho_da_populacao] = populacao[melhor_solucao]
    fitness_populacao_futura[tamanho_da_populacao] = fitness[melhor_solucao]

def identifica_pior_solucao_da_populacao_futura():
    pior_solucao = 0
    for i in range(tamanho_da_populacao+1):
        if fitness_populacao_futura[pior_solucao] > fitness_populacao_futura[i]:
            pior_solucao = i
    return pior_solucao

def gerar_solucao_inicial():
    for i in range(tamanho_da_populacao):
        for j in range(tamanho_solucao):
            populacao[i][j] = random.randint(0, 1)

def identifica_pior_solucao_da_populacao_atual():
    pior_solucao = 0
    for i in range(tamanho_da_populacao):
        if fitness[pior_solucao] > fitness[i]:
            pior_solucao = i
    return pior_solucao

def gerar_populacao_futura():
    pior = identifica_pior_solucao_da_populacao_futura()
    del populacao_futura[pior]
    del fitness_populacao_futura[pior]

    populacao = populacao_futura
    fitness = fitness_populacao_futura

    populacao_futura.append(populacao_futura[0])
    fitness_populacao_futura.append(fitness_populacao_futura[0])

def criterio_de_parada_atingido(avaliacoes_atual):
    return avaliacoes_atual >= avaliacoes_total

def relatorio_de_convergencia_da_geracao():
    melhor_fitness.append(fitness[identifica_melhor_solucao()])
    pior_fitness.append(fitness[identifica_pior_solucao_da_populacao_atual()])
    media = 0
    for i in fitness:
        media = media+i
    media_fitness.append(media/len(fitness))

def determina_pais():
    mae = random.randint(0, 3)
    pai = random.randint(0, 3)
    while mae == pai:
        pai = random.randint(0, 3)
    return [mae, pai]

def cruzamento():
    parente = determina_pais()
    pai = populacao[parente[0]]
    mae = populacao[parente[1]]
    ponto_cruzamento = random.randint(0, 5)
    filho1 = [0] * len(mae)
    filho2 = [0] * len(mae)

    for i in range(len(mae)):
        if i <= ponto_cruzamento:
            filho1[i] = mae[i]
            filho2[i] = pai[i]
        else:
            filho1[i] = pai[i]
            filho2[i] = mae[i]
    populacao[parente[0]] = filho1
    populacao[parente[1]] = filho2

def startAlgoritm():
    gerar_solucao_inicial()
    avaliar_populacao()
    avaliacoes_atual = tamanho_da_populacao
    relatorio_de_convergencia_da_geracao()
    contador = 0
    while not criterio_de_parada_atingido(avaliacoes_atual):
        elitismo()
        for i in range(tamanho_da_populacao):
            cruzamento()
            mutacao(i)
            fitness_populacao_futura[i] = objetivo(populacao_futura[i])
            avaliacoes_atual = avaliacoes_atual + 1
        gerar_populacao_futura()
        relatorio_de_convergencia_da_geracao()
        contador = contador + 1
    melhor_final = identifica_melhor_solucao()
    print("Melhor individuo", populacao[melhor_final],"Fitness =",fitness[melhor_final],'\n')

contador2 = 10
while contador2 >= 0:
    startAlgoritm()
    contador2 = contador2 - 1