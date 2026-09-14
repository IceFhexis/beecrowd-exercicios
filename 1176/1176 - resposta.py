fibonacci = [0, 1]

for indice in range(2, 51):
    fibonacci.append(fibonacci[indice - 1] + fibonacci[indice - 2])

casos = int(input())

for _ in range(casos):
    indice = int(input())
    print(f"Fib({indice}) = {fibonacci[indice]}")