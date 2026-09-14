# ler os tres valores de ponto flutuante e
# calcular as raizes com a formula de Bhaskara

# usa a biblioteca math para calcular a raiz
from math import sqrt

# lê os três valores e converte cada um para float
a, b, c = map(float, input().split())

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)

    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')