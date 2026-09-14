# ler um valor n e retornar n linhas
# cada linha possui 3 números seguidos de PUM

n = int(input())

numero = 1

for i in range(n):
    print(numero, numero + 1, numero + 2, "PUM")

    numero += 4