casos = int(input())

for _ in range(casos):
    primeiro, segundo = map(int, input().split())
    inicio, fim = sorted((primeiro, segundo))
    soma = sum(numero for numero in range(inicio + 1, fim) if numero % 2 != 0)
    print(soma)