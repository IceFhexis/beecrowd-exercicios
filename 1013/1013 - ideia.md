# 1013 - O Maior

## Ideia

Ler 3 números inteiros e calcular o maior deles utilizando a fórmula:

`maior = (a + b + abs(a - b)) / 2`

Essa fórmula calcula o maior entre dois números. Por isso, primeiro calculamos o maior entre `A` e `B` e depois usamos o resultado para calcular o maior entre ele e `C`.

## Passos

1. Ler `A`, `B` e `C`.
2. Calcular o maior entre `A` e `B` utilizando a fórmula.
3. Calcular o maior entre o resultado anterior e `C` utilizando a mesma fórmula.
4. Imprimir o maior seguido de `"eh o maior"`.

## Pseudocódigo

```text
leia A, B, C

maiorAB <- (A + B + |A - B|) / 2

maiorABC <- (maiorAB + C + |maiorAB - C|) / 2

mostre maiorABC, "eh o maior"