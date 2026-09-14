salario = float(input())
reajuste = 0

if salario <= 400:
    reajuste = 0.15
elif salario <= 800:
    reajuste = 0.12
elif salario <= 1200:
    reajuste = 0.1
elif salario <= 2000:
    reajuste = 0.07
else:
    reajuste = 0.04

novo_salario = salario * (1 + reajuste)
ganho = novo_salario - salario
percentual = int(reajuste * 100)

print('Novo salario:', f'{novo_salario:.2f}')
print('Reajuste ganho:', f'{ganho:.2f}')
print('Em percentual:', f'{percentual} %')
