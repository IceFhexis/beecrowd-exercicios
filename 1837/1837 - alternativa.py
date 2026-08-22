# 1. Ler a e b
a, b = map(int, input().split())

# 2. O resto euclidiano sempre fica positivo usando o valor absoluto de b
r = a % abs(b)

# 3. Descobrir o quociente correto a partir do resto corrigido
q = (a - r) // b

# 4. Imprimir resultado
print(q, r)