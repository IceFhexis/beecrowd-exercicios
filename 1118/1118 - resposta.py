while True:
    notas = []

    while len(notas) < 2:
        nota = float(input())

        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("nota invalida")

    print(f"media = {sum(notas) / 2:.2f}")
    print("novo calculo (1-sim 2-nao)")

    if int(input()) == 2:
        break