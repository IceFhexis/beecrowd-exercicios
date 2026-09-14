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

a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    a2 = a ** 2
    soma = b ** 2 + c ** 2

    if a2 == soma:
        print("TRIANGULO RETANGULO")
    elif a2 > soma:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c:
        print("TRIANGULO ISOSCELES")