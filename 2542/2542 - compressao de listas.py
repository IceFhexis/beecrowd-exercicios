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
        qtd_atributos = int(input())

        qtd_M, qtd_L = map(int, input().split())

        cartas_M = [
            list(map(int, input().split()))
            for _ in range(qtd_M)
        ]

        cartas_L = [
            list(map(int, input().split()))
            for _ in range(qtd_L)
        ]

        escolha_M, escolha_L = map(int, input().split())
        escolha_atributo = int(input())

        valor_M = cartas_M[escolha_M - 1][escolha_atributo - 1]
        valor_L = cartas_L[escolha_L - 1][escolha_atributo - 1]

        if valor_M > valor_L:
            print("Marcos")
        elif valor_M < valor_L:
            print("Leonardo")
        else:
            print("Empate")

    except EOFError:
        break