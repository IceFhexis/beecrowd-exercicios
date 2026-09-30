from random import randint

valor = randint(0,9)

media = []

while not valor == 0:
    media.append(valor)
    valor = randint(0,9)

if not media:
    media.append(0)

print(f'{sum(media)/len(media):.1f}')
