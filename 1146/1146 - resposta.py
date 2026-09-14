# ler os numeros até uma condição ser atingida (loop)
# e mostrar uma sequencia começando do 1 até o numero next
# para quando o numero for 0
"""
1. Leia um número.

2. Enquanto ele não for 0:
      conte de 1 até esse número
      e mostre cada valor.

3. Leia outro número e repita.

"""

# ler um número
numero = int(input())

# continuar enquanto o número for diferente de zero
while numero != 0:

    # contar de 1 até o número digitado
    for contador in range(1, numero + 1):

        # se for o último número, imprimir sem espaço no final
        if contador == numero:
            print(contador)

        # caso contrário, imprimir o número seguido de espaço
        else:
            print(contador, end=" ")

    # ler o próximo número
    numero = int(input())