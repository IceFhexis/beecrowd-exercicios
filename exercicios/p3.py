num = int(input())

cont = 1
p = True

for i in range(2, num):
    if(num%i == 0):
        p = False
        break

print("primo" if p else "nao primo")
