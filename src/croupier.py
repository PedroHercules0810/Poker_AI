import random

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
    valores = list(range(1, 14))
    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    random.shuffle(baralho)

    # Distribuir cartas para os jogadores
    mao_jogadores = [baralho[i:i+num_cartas_jogador] for i in range(0, num_jogadores*num_cartas_jogador, num_cartas_jogador)]
    baralho = baralho[num_jogadores*num_cartas_jogador:]

    # Distribuir cartas comunitárias
    cartas_comunitarias = baralho[:num_cartas_comunitarias]

    return mao_jogadores, cartas_comunitarias

# Exemplo de uso para um jogo de Texas Hold'em:
num_jogadores = 4
num_cartas_jogador = 2
num_cartas_comunitarias = 5

maos, comunitarias = distribuir_cartas(num_jogadores, num_cartas_jogador, num_cartas_comunitarias)
print("Mãos dos jogadores:", maos)
print("Cartas comunitárias:", comunitarias)
