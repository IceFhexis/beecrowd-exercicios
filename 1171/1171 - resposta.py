quantidade = int(input())
frequencias = {}

for _ in range(quantidade):
    numero = int(input())
    frequencias[numero] = frequencias.get(numero, 0) + 1

for numero in sorted(frequencias):
    print(f"{numero} aparece {frequencias[numero]} vez(es)")