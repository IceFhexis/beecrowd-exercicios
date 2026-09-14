while True:
    N = int(input())
    if N == 0:
        break

    for i in range(N):
        linha = []
        for j in range(N):
            valor = abs(i - j) + 1
            linha.append(f"{valor:3d}")

        # Junta os números com espaço, sem deixar espaço no final
        print(" ".join(linha))

    # Linha em branco após cada matriz
    print()
