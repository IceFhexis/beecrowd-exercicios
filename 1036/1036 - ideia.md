# 1036 - Formula de Bhaskara

## Ideia
Usar a formula de Bhaskara para encontrar as duas raizes de uma equacao do segundo grau: `x = (-b +- sqrt(delta)) / (2a)`, em que `delta = b^2 - 4ac`.

## Casos importantes
- Se `a` for zero, a equacao nao e do segundo grau.
- Se `delta` for negativo, nao existem raizes reais.
- Nos dois casos, imprimir `Impossivel calcular`.

## Passos
1. Ler `a`, `b` e `c`.
2. Calcular o discriminante.
3. Verificar se o calculo e possivel.
4. Calcular `R1` e `R2` e mostrar cada uma com 5 casas decimais.
