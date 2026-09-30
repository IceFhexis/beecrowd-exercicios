hora_ini, hora_fim = map(int, input().split())

tempo = 0

if hora_fim > hora_ini:
    tempo = hora_fim - hora_ini
elif hora_ini > hora_fim:
    tempo = abs(hora_ini - 24) + hora_fim
else:
    tempo = 24

print(f'O JOGO DUROU {tempo} HORA(S)')
