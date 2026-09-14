# ler quatro números e calcular média com pesos
# retornar o estado do aluno

n1, n2, n3, n4 = map(float, input().split())

# pesos: 2, 3, 4 e 1
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

print('Media:', f'{media:.1f}')

if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

else:
    print('Aluno em exame.')

    exame = float(input())

    print('Nota do exame:', f'{exame:.1f}')

    media_final = (media + exame) / 2

    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print('Media final:', f'{media_final:.1f}')