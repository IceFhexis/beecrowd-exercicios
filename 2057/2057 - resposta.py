# pega a hora de saida, o tempo de viagem e o fuso horario
saida, tempo_viagem, fuso = input().split()

# calcula a hora de chegada
chegada = int(saida) + int(tempo_viagem) + int(fuso)

# ajusta a hora caso passe da meia-noite
if chegada >= 24:
    chegada -= 24
elif chegada < 0:
    chegada += 24

print(chegada)