tempo = int(input())


segundos = tempo % 60
minutos = (tempo // 60) % 60
horas = tempo // 3600

print(f'{horas}:{minutos}:{segundos}')