# ler os tres valores de ponto flutuante e
# calcular as raizes com a formula de Bhaskara

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

# formula do discriminante
delta = (b**2) - 4*a*c

# casos impossiveis
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    x1 = (-b + delta ** (1/2)) / (2*a)
    x2 = (-b - delta ** (1/2)) / (2*a)
    
    # Imprime com 5 casas decimais
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')