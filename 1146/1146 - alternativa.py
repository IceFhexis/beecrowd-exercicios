# ler os numeros até uma condição ser atingida (loop)
# e mostrar uma sequencia começando do 1 até o numero next
# para quando o numero for 0

numero = int(input())

while numero != 0:
    numeros = range(1, numero + 1)

    print(*numeros)

    numero = int(input())