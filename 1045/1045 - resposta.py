# classifique os triangulos quanto a seus lados e angulos
#
# 1. Ler A, B e C
#        ↓
# 2. Garantir que A seja o maior
#        ↓
# 3. Forma triângulo?
#       NÃO → NAO FORMA TRIANGULO
#       SIM → classifica ângulos
#             + classifica lados

# ler os três lados
a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

# colocar o maior valor em A
if b > a:
    auxiliar = a
    a = b
    b = auxiliar

if c > a:
    auxiliar = a
    a = c
    c = auxiliar

# verificar se forma um triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    # classificar pelos ângulos
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")

    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")

    else:
        print("TRIANGULO ACUTANGULO")

    # classificar pelos lados
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")