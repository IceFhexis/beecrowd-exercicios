# 1837 - Prefácio

# Ideia
Calcular o quociente `q` e o resto `r` de uma divisão entre dois números `a` e `b`. A única regra obrigatória do problema é que **o resto `r` nunca pode ser negativo** (deve ser maior ou igual a zero e menor que o valor absoluto de `b`).

# Passos
1. Ler os dois números inteiros `a` e `b`.
2. Calcular o quociente `q` e o resto `r` usando a divisão padrão do Python.
3. Se o resto `r` for negativo, ajustar `q` e `r` para que o resto fique positivo.
4. Imprimir o resultado de `q` e `r`.

# Pseudocodigo
```text
Ler a e b

Calcular q (a dividido por b)
Calcular r (resto de a por b)

Se r for menor que 0:
    Se b for positivo:
        Subtrair 1 de q
        Somar b em r
    Se b for negativo:
        Somar 1 de q
        Subtrair b em r

Imprimir q e r
```