# 1012 - Área

## Ideia
Ler 3 números com ponto flutuante e calcular todas as áreas pedidas.

## Passos
1. Ler `A`, `B` e `C`.
2. Calcular a área do triângulo retângulo de base `A` e altura `C`.
3. Calcular a área do círculo de raio `C`.
4. Calcular a área do trapézio de bases `A` e `B` e altura `C`.
5. Calcular a área do quadrado de lado `B`.
6. Calcular a área do retângulo de lados `A` e `B`.
7. Imprimir as áreas com 3 casas decimais.

## Pseudocódigo
```text
leia A, B, C

triangulo <- (A * C) / 2
circulo <- 3.14159 * C²
trapezio <- ((A + B) * C) / 2
quadrado <- B²
retangulo <- A * B

mostre "TRIANGULO:", triangulo
mostre "CIRCULO:", circulo
mostre "TRAPEZIO:", trapezio
mostre "QUADRADO:", quadrado
mostre "RETANGULO:", retangulo