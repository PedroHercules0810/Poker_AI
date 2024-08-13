import random

def distribuir_cartas(num_jogadores):
    """
    Distribui duas cartas únicas para cada jogador em um jogo de cartas.

    Args:
        num_jogadores: O número de jogadores.

    Returns:
        Uma lista de listas, onde cada lista interna representa as cartas de um jogador.
    """

    naipes = ['P', 'C', 'O', 'E']  # Paus, Copas, Ouros, Espadas
    valores = list(range(1, 14))

    baralho = [(valor, naipe) for naipe in naipes for valor in valores]
    random.shuffle(baralho)

    cartas_por_jogador = 2
    mao_jogadores = [baralho[i:i+cartas_por_jogador] for i in range(0, num_jogadores*cartas_por_jogador, cartas_por_jogador)]

    return mao_jogadores

# Exemplo de uso:
num_jogadores = 26
maos = distribuir_cartas(num_jogadores)
print(maos)
