# ler a hora e descobrir o atraso maximo

while True:
    try:
        # extrai a hora e minuto da entrada -> X:XX
        horas, minutos = input().split(':')

        # horario combinado: 8:00
        hora_saida_terminal = 8 * 60

        # converte tudo em minutos
        tempo_acordou = (int(horas) * 60) + int(minutos)

        # pior caso: leva 60 minutos para chegar
        hora_chegada_terminal = tempo_acordou + 60

        if hora_chegada_terminal <= hora_saida_terminal:
            print('Atraso maximo:', 0)

        else:
            atraso = hora_chegada_terminal - hora_saida_terminal
            print('Atraso maximo:', atraso)
    
    # encerra no requiso do beecrowd
    except EOFError:
        break