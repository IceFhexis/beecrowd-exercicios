"""
1. lê N
2. lê M e L
3. lê M cartas de Marcos
4. lê L cartas de Leonardo
5. lê as cartas escolhidas
6. lê o atributo
7. compara
8. começa outro caso de teste

"""

while True:
    try:
        # quantidade de atributos de cada carta
        qtd_atributos = int(input())

        # quantidade de cartas de Marcos e Leonardo
        qtd_M, qtd_L = map(int, input().split())

        cartas_M = []
        cartas_L = []

        # ler as cartas de Marcos
        for i in range(qtd_M):
            carta = list(map(int, input().split()))
            cartas_M.append(carta)

        # ler as cartas de Leonardo
        for i in range(qtd_L):
            carta = list(map(int, input().split()))
            cartas_L.append(carta)

        # cartas escolhidas
        escolha_M, escolha_L = map(int, input().split())

        # atributo sorteado
        escolha_atributo = int(input())

        # pegar o valor do atributo escolhido
        atributo_M = cartas_M[escolha_M - 1][escolha_atributo - 1]
        atributo_L = cartas_L[escolha_L - 1][escolha_atributo - 1]

        # descobrir o vencedor
        if atributo_M > atributo_L:
            print("Marcos")

        elif atributo_M < atributo_L:
            print("Leonardo")

        else:
            print("Empate")

    except EOFError:
        break