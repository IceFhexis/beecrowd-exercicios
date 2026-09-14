valor = int(round(float(input()) * 100))

print("NOTAS:")
for denominacao in [10000, 5000, 2000, 1000, 500, 200]:
    quantidade = valor // denominacao
    print(f"{quantidade} nota(s) de R$ {denominacao / 100:.2f}")
    valor -= quantidade * denominacao

print("MOEDAS:")
for denominacao in [100, 50, 25, 10, 5, 1]:
    quantidade = valor // denominacao
    print(f"{quantidade} moeda(s) de R$ {denominacao / 100:.2f}")
    valor -= quantidade * denominacao