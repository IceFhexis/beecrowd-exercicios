# outra forma de fazer usando o resto da divisão por 24
# assim o resultado sempre fica entre 0 e 23

saida, tempo_viagem, fuso = input().split()

chegada = (int(saida) + int(tempo_viagem) + int(fuso)) % 24

print(chegada)