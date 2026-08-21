v = int(input())

digitos = "0123456789ABCDEF"
hexadecimal = ""

while v > 0:
    resto = v % 16

    hexadecimal = digitos[resto] + hexadecimal

    v = v // 16

print(hexadecimal)