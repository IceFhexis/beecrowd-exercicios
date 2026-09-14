# alternativa usando uma lista com os pares de DDD e cidade

codigos = [
    ['61', 'Brasilia'],
    ['11', 'Sao Paulo'],
    ['71', 'Salvador'],
    ['21', 'Rio de Janeiro'],
    ['32', 'Juiz de Fora'],
    ['19', 'Campinas'],
    ['27', 'Vitoria'],
    ['31', 'Belo Horizonte']
]

ddd = input()

cidade = None

for codigo in codigos:
    if codigo[0] == ddd:
        cidade = codigo[1]
        break

if cidade:
    print(cidade)
else:
    print('DDD nao cadastrado')