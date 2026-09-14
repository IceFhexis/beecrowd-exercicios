n = int(input())
paisagens = list(map(int, input().split()))

resultado = 1

for i in range(1, n):
    if paisagens[i] == paisagens[i - 1]:
        resultado = 0
        break

    if i > 1:
        if (paisagens[i] > paisagens[i - 1]) == (paisagens[i - 1] > paisagens[i - 2]):
            resultado = 0
            break

print(resultado)