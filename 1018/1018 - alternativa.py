dinheiro = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = dinheiro // nota
    print(f'{quantidade} nota(s) de R$ {nota},00')
    dinheiro -= quantidade * nota