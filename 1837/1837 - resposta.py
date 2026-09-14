# 1. Ler a e b
a, b = map(int, input().split())

# 2. Calcular q e r padrão do Python
q = a // b
r = a % b

# 3. Ajustar se o resto for negativo (Regra da Divisão Euclidiana)
if r < 0:
    if b > 0:
        q = q - 1
        r = r + b
    else:
        q = q + 1
        r = r - b

# 4. Imprimir resultado
print(q, r)