# Lê o número como texto para preservar o sinal de -0
entrada = input()

# Converte para float
numero = float(entrada)

# Determina o sinal olhando a entrada original
sinal = "-" if entrada.startswith("-") else "+"

# Trabalha com o valor absoluto do número
numero = abs(numero)

# O expoente começa em zero
expoente = 0

# Divide por 10 até o número ficar menor que 10
while numero >= 10:
    numero /= 10
    expoente += 1

# Multiplica por 10 até o número ficar maior ou igual a 1
while numero < 1 and numero != 0:
    numero *= 10
    expoente -= 1

# Determina o sinal do expoente
sinal_expoente = "+" if expoente >= 0 else "-"

# Pega o valor absoluto do expoente
expoente = abs(expoente)

# Imprime usando a formatação pedida
print(sinal, f"{numero:.4f}", "E", sinal_expoente, f"{expoente:02d}", sep="")