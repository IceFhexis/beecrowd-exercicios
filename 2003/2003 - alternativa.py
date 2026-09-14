# ler a hora e descobrir o atraso maximo

while True:
    try:
        horas, minutos = input().split(':')

        horas = int(horas)
        minutos = int(minutos)

        tempo_acordou = horas * 60 + minutos

        atraso = tempo_acordou + 60 - 480

        if atraso < 0:
            atraso = 0

        print('Atraso maximo:', atraso)

    except EOFError:
        break