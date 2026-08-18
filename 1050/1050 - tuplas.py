# alternativa usando tuplas

codigos = [
    ('61', 'Brasilia'),
    ('11', 'Sao Paulo'),
    ('71', 'Salvador'),
    ('21', 'Rio de Janeiro'),
    ('32', 'Juiz de Fora'),
    ('19', 'Campinas'),
    ('27', 'Vitoria'),
    ('31', 'Belo Horizonte')
]

ddd = input()

for codigo, cidade in codigos:
    if codigo == ddd:
        print(cidade)
        break
else:
    print('DDD nao cadastrado')