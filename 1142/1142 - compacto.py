# ler um valor n e retornar n linhas
# cada linha possui 3 números seguidos de PUM

n = int(input())

for i in range(1, n * 4, 4):
    print(i, i + 1, i + 2, "PUM")