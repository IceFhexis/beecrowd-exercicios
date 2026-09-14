while True:
    tamanho = int(input())

    if tamanho == 0:
        break

    for linha in range(tamanho):
        valores = [f"{abs(linha - coluna) + 1:3d}" for coluna in range(tamanho)]
        print(" ".join(valores))

    print()