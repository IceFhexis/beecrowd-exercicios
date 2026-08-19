valor_antigo, valor_novo = map(float, input().split())

aumento = (valor_novo - valor_antigo) / valor_antigo * 100

print(f'{aumento:.2f}%')