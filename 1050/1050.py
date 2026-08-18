# let ddd e retornar o nome do estado

def main():

    #usando dicionario
    codigos = {
        '61': {'nome': 'Brasilia'},
        '11': {'nome': 'Sao Paulo'},
        '71': {'nome': 'Salvador'},
        '21': {'nome': 'Rio de Janeiro'},
        '32': {'nome': 'Juiz de fora'},
        '19': {'nome': 'Campinas'},
        '27': {'nome': 'Vitoria'},
        '31': {'nome': 'Belo Horizonte'}
    }

    ddd = input()

    if(not ddd):
        return

    if(ddd not in codigos):
        print('DDD nao cadastrado')
        return

    print(codigos[ddd]['nome'])

if __name__ == "__main__":
    main()
