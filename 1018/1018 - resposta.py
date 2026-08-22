# Ler a quantia

dinheiro = int(input())

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

print(dinheiro)

#Nota de 100
nota_100 += dinheiro // 100

#Retira a parte separada
dinheiro -= nota_100 * 100

#Nota de 50
nota_50 += dinheiro // 50

#Retira a parte separada
dinheiro -= nota_50 * 50

# ...
nota_20 += dinheiro // 20

# ...
dinheiro -= nota_20 * 20

nota_10 += dinheiro // 10

dinheiro -= nota_10 * 10

nota_5 += dinheiro // 5

dinheiro -= nota_5 * 5

nota_2 += dinheiro // 2

dinheiro -= nota_2 * 2

nota_1 += dinheiro // 1

print(f'{nota_100} nota(s) de R$ 100,00')
print(f'{nota_50} nota(s) de R$ 50,00')
print(f'{nota_20} nota(s) de R$ 20,00')
print(f'{nota_10} nota(s) de R$ 10,00')
print(f'{nota_5} nota(s) de R$ 5,00')
print(f'{nota_2} nota(s) de R$ 2,00')
print(f'{nota_1} nota(s) de R$ 1,00')