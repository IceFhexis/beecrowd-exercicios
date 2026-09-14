# calcula a área de um círculo a partir do raio

# valor aproximado de pi, dado pela questão
pi = 3.14159

# lê o raio e converte o valor para float
raio = float(input())

# fórmula da área do círculo: A = pi * r²
area = pi * raio**2

# exibe o resultado com 4 casas decimais
print("A=", f"{area:.4f}", sep='')