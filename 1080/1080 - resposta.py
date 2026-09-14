maior = None
posicao_maior = 0

for posicao in range(1, 101):
    valor = int(input())

    if maior is None or valor > maior:
        maior = valor
        posicao_maior = posicao

print(maior)
print(posicao_maior)