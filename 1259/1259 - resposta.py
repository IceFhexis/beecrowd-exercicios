quantidade = int(input())
pares = []
impares = []

for _ in range(quantidade):
    numero = int(input())
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

for numero in sorted(pares):
    print(numero)

for numero in sorted(impares, reverse=True):
    print(numero)