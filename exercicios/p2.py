num = int(input())

fat = []
res = 1

for i in range(1, num):
    fat.append(i)
    res *= i

print(fat)
#print(f'Imprime apenas os 5 primeiros {fat[:5]}')
print(res)
