n = int(input())

fib = []

for i in range(n):
    fib.append(i if i < 2 else fib[i-2] + fib[i-1])

print(*fib)
