# alternativa usando listas

ddds = ['61', '11', '71', '21', '32', '19', '27', '31']

cidades = [
    'Brasilia',
    'Sao Paulo',
    'Salvador',
    'Rio de Janeiro',
    'Juiz de Fora',
    'Campinas',
    'Vitoria',
    'Belo Horizonte'
]

ddd = input()

if ddd in ddds:
    indice = ddds.index(ddd)
    print(cidades[indice])
else:
    print('DDD nao cadastrado')