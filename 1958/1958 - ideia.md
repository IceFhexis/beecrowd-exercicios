# 1958 - Notação Científica

## Ideia

Converter um número de ponto flutuante para **notação científica** manualmente.

Na notação científica, o número deve ficar no formato:

`N × 10^expoente`

Onde `N` deve ficar entre `1` e `10`.

Por exemplo:

`1234.5 = 1.2345 × 10³`

`0.0123 = 1.23 × 10⁻²`

Para fazer essa conversão, podemos dividir ou multiplicar o número por `10` até ele ficar entre `1` e `10`, contando quantas vezes isso foi feito.

---

## Passos

1. Ler o número.
2. Guardar o sinal do número (`+` ou `-`).
3. Pegar o valor absoluto do número.
4. Criar uma variável `expoente` começando em `0`.
5. Enquanto o número for maior ou igual a `10`:
   - Dividir o número por `10`.
   - Somar `1` ao expoente.
6. Enquanto o número for menor que `1` e diferente de `0`:
   - Multiplicar o número por `10`.
   - Subtrair `1` do expoente.
7. Determinar o sinal do expoente.
8. Imprimir o número no formato da notação científica.

---

## Pseudocódigo

```text
Ler numero

Se numero for maior ou igual a 0:
    sinal = "+"
Senão:
    sinal = "-"

numero = valor absoluto de numero

expoente = 0

Enquanto numero >= 10:
    numero = numero / 10
    expoente = expoente + 1

Enquanto numero < 1 e numero diferente de 0:
    numero = numero * 10
    expoente = expoente - 1

Se expoente >= 0:
    sinal_expoente = "+"
Senão:
    sinal_expoente = "-"

expoente = valor absoluto de expoente

Imprimir sinal, numero, "E", sinal_expoente e expoente