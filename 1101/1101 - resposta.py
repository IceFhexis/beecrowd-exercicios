while True:
    primeiro, segundo = map(int, input().split())

    if primeiro <= 0 or segundo <= 0:
        break

    inicio, fim = sorted((primeiro, segundo))
    valores = list(range(inicio, fim + 1))
    print(*valores, f"Sum={sum(valores)}")