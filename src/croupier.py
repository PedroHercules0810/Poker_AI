import random
from itertools import combinations

def distribuir_cartas(num_jogadores, num_cartas_jogador, num_cartas_comunitarias):
    """
    Distribui cartas para jogadores e uma mesa comunitária.

    Args:
        num_jogadores: Número de jogadores.
        num_cartas_jogador: Número de cartas por jogador.
        num_cartas_comunitarias: Número de cartas comunitárias.

    Returns:
        Uma tupla com duas listas:
            * mao_jogadores: Uma lista de listas, onde cada lista interna representa as cartas de um jogador.
            * cartas_comunitarias: Uma lista com as cartas comunitárias.
    """

    naipes = ['P', 'C', 'O', 'E']
    valores = list(range(2, 15))  # Valores de 2 a Ás (14)
    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    random.shuffle(baralho)

    mao_jogadores = [baralho[i:i+num_cartas_jogador] for i in range(0, num_jogadores*num_cartas_jogador, num_cartas_jogador)]
    baralho = baralho[num_jogadores*num_cartas_jogador:]
    cartas_comunitarias = baralho[:num_cartas_comunitarias]

    return mao_jogadores, cartas_comunitarias

def classificar_mao(mao):
    """
    Classifica uma mão de 5 cartas de poker.

    Args:
        mao: Uma lista de tuplas (valor, naipe) representando as 5 cartas.

    Returns:
        Uma tupla (classificacao, descricao), onde classificacao é um número inteiro 
        representando a força da mão e descricao é uma string com o nome da mão.
    """

    mao = sorted(mao, key=lambda x: x[0], reverse=True)  # Ordena a mão por valor
    naipes = set([carta[1] for carta in mao])
    valores = [carta[0] for carta in mao]

    # Verifica se é um flush
    if len(naipes) == 1:
        # Verifica se é um straight
        if valores == list(range(valores[0], valores[0]-5, -1)):
            if valores[0] == 14:  # Royal Flush
                return 10, "Royal Flush"
            else:
                return 9, "Straight Flush"
        # ... (implementar outras verificações, como quadra, full house, etc.)

    # ... (implementar outras verificações de mão)

    # Se não for nenhum dos casos acima, retorna High Card
    return 1, "High Card"

def analisar_maos(mao_jogadores, cartas_comunitarias):
    """
    Analisa as mãos de poker e determina o vencedor.

    Args:
        mao_jogadores: Uma lista de listas, onde cada lista interna representa as cartas de um jogador.
        cartas_comunitarias: Uma lista com as cartas comunitárias.

    Returns:
        Uma lista de tuplas (jogador, melhor_mao, classificacao), onde cada tupla representa o jogador, 
        a melhor mão e a classificação da mão.
    """

    melhores_maos = []
    for i, mao_jogador in enumerate(mao_jogadores):
        todas_combinacoes = combinations(mao_jogador + cartas_comunitarias, 5)
        melhor_mao_jogador = None
        melhor_classificacao = 0
        for combinacao in todas_combinacoes:
            classificacao, descricao = classificar_mao(combinacao)
            if classificacao > melhor_classificacao:
                melhor_mao_jogador = combinacao
                melhor_classificacao = classificacao
        melhores_maos.append((i, melhor_mao_jogador, melhor_classificacao))

    melhores_maos.sort(key=lambda x: x[2], reverse=True)
    return melhores_maos

# Exemplo de uso para um jogo de Texas Hold'em:
num_jogadores = 7
num_cartas_jogador = 2
num_cartas_comunitarias = 5

maos, comunitarias = distribuir_cartas(num_jogadores, num_cartas_jogador, num_cartas_comunitarias)
resultado = analisar_maos(maos, comunitarias)

# Imprimindo os resultados
print("Cartas Comunitárias:", comunitarias)

for jogador, (melhor_mao, classificacao) in enumerate(resultado):
    if melhor_mao is None:
        print(f"Jogador {jogador+1}: Sem mão válida")
    else:    
        print(f"Jogador {jogador+1}: {melhor_mao} - Classificação: {classificacao}")