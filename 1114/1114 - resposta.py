# repetir os comandos até que a senha seja valida

# senha correta
senha_valida = 2002

# ler a primeira tentativa
senha_digitada = int(input())

# enquanto a senha estiver errada
while senha_digitada != senha_valida:
    print("Senha Invalida")

    # pedir uma nova senha
    senha_digitada = int(input())

# quando sair do while, significa que a senha está correta
print("Acesso Permitido")