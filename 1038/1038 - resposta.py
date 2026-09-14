itens = [
    [1, 4.0],
    [2, 4.5],
    [3, 5.0],
    [4, 2.0],
    [5, 1.5]
]

codigo, qtd = map(int, input().split())

produto = itens[codigo - 1][1]

print(f'Total: R$ {produto * qtd:.2f}')