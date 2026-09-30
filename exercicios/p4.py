x = int(input())

if(x == 0 or (x%10 == 0 and x != 0)):
    palindromo = False
else:
    original = x
    soma_r = 0

    while x > 0:
        digito = x % 10
        soma_r = (soma_r * 10) + digito
        x //= 10
        #print(original, x, soma_r, digito)

    palindromo = (soma_r == original)

print("palindromo" if palindromo else "Nop")
