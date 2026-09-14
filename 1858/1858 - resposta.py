quantidade = int(input())
valores = list(map(int, input().split()))

menor = min(valores[:quantidade])
print(valores.index(menor) + 1)