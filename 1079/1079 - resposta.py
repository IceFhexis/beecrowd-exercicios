casos = int(input())

for _ in range(casos):
    notas = [float(valor) for valor in input().split()]
    media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 5) / 10
    print(f"{media:.1f}")