# 1478 - Quadrado Magico

## Ideia
Cada elemento da matriz e a distancia entre sua linha e coluna, mais 1. A leitura termina quando o tamanho informado for zero.

## Passos
1. Ler o tamanho `N`.
2. Para cada posicao `(linha, coluna)`, calcular `abs(linha - coluna) + 1`.
3. Imprimir cada valor com largura 3.
4. Imprimir uma linha em branco apos cada matriz e encerrar com `N = 0`.