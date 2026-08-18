# Solução alternativa
# outra forma de resolver usando dicionário
# pouco do que está presente aqui não vimos isso em aula, 
# porém dá uma perspectiva mais ampla da resolução dos problemas

codigos = {
    '61': 'Brasilia',
    '11': 'Sao Paulo',
    '71': 'Salvador',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte'
}

ddd = input()

if ddd in codigos:
    print(codigos[ddd])
else:
    print('DDD nao cadastrado')