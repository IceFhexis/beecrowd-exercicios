valores = [int(input()) for _ in range(20)]

for indice in range(19, -1, -1):
    print(f"N[{19 - indice}] = {valores[indice]}")