# ler o tempo total em segundos
tempo = int(input())

# descobrir quantas horas completas existem
horas = tempo // 3600

# retirar as horas e guardar os segundos restantes
resto = tempo % 3600

# descobrir quantos minutos completos existem no restante
minutos = resto // 60

# o que sobrar são os segundos
segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')