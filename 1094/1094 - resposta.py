casos = int(input())
coelhos = 0
ratos = 0
sapos = 0

for _ in range(casos):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)

    if tipo == "C":
        coelhos += quantidade
    elif tipo == "R":
        ratos += quantidade
    else:
        sapos += quantidade

total = coelhos + ratos + sapos

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / total * 100:.2f} %")
print(f"Percentual de ratos: {ratos / total * 100:.2f} %")
print(f"Percentual de sapos: {sapos / total * 100:.2f} %")