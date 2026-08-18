# pegar hora de saida, tempo de viagem e fuso horario, retornar a hora de chegada
# 24 -> meia noite -> 0

saida, tempo_viagem, fuso = input().split(' ')


chegada = int(saida) + int(tempo_viagem) + int(fuso)

if chegada > 24:
    chegada -= 24
elif chegada < 0:
    chegada += 24 

print(chegada)
