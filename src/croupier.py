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

    mao = sorted(mao, key=lambda x: x[0], reverse=True)
    valores = [carta[0] for carta in mao]
    naipes = [carta[1] for carta in mao]

    # Conta a frequência de cada valor
    contagem_valores = {}
    for valor in valores:
        contagem_valores[valor] = contagem_valores.get(valor, 0) + 1

    # Verifica as mãos
    if all(naipes[i] == naipes[0] for i in range(5)):  # Flush
        if valores == list(range(valores[0], valores[0]-5, -1)):  # Straight flush
            if valores[0] == 14:  # Royal flush
                return 10, "Royal Flush"
            return 9, "Straight Flush"
        # Check for straight flush with Ace low
        elif valores == [14, 5, 4, 3, 2]:
            return 9, "Straight Flush (Ace Low)"
        return 6, "Flush"
    # ... (implementar outras verificações, como quadra, full house, etc.)

    # Verifica quadra
    if 4 in contagem_valores.values():
        return 8, "Quadra"

    # Verifica full house
    if 3 in contagem_valores.values() and 2 in contagem_valores.values():
        return 7, "Full House"

    # Verifica trinca
    if 3 in contagem_valores.values():
        return 4, "Trinca"

    # Verifica dois pares
    if list(contagem_valores.values()).count(2) == 2:
        return 3, "Dois Pares"

    # Verifica um par
    if 2 in contagem_valores.values():
        return 2, "Um Par"

    # Verifica straight
    if valores == list(range(valores[0], valores[0]-5, -1)):
        return 5, "Straight"

    # High card
    return 1, "High Card"

def encontrar_vencedor(classificacoes):
    melhor_classificacao = max(classificacoes, key=lambda x: x[0])
    vencedores = [i for i, classificacao in enumerate(classificacoes) if classificacao == melhor_classificacao]
    return vencedores

num_cartas_jogador = 2
num_cartas_comunitarias = 5

print("Quantos jogadores irão jogar?")
num_jogadores = input()

num_jogadores = int(num_jogadores)

maos, comunitarias = distribuir_cartas(num_jogadores, num_cartas_jogador, num_cartas_comunitarias)

# Imprimindo os resultados
print("Cartas Comunitárias:", comunitarias)

for i in range(num_jogadores):
    mao_jogador = maos[i]
    mao_completa = mao_jogador + comunitarias
    classificacao, descricao = classificar_mao(mao_completa)
    print(f"Jogador {i+1}: {mao_jogador} = {descricao}")
    

classificacoes_jogadores = []
for i in range(num_jogadores):
    mao_jogador = maos[i]
    mao_completa = mao_jogador + comunitarias
    classificacao, descricao = classificar_mao(mao_completa)
    classificacoes_jogadores.append((classificacao, descricao))

vencedores = encontrar_vencedor(classificacoes_jogadores)
# Retornando o índice do primeiro vencedor (se houver empate)
if vencedores:
    vencedor = vencedores[0]
    print(f"O vencedor é o jogador {vencedor+1}")
else:
    print("Não houve vencedor.")


