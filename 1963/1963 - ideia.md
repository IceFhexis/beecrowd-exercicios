# 1963 - O Filme

## Ideia
Ler dois valores e calcular o aumento percentual do segundo valor em relação ao primeiro.

## Passos
1. Ler o valor antigo e o valor novo.
2. Calcular a diferença entre os dois valores.
3. Dividir a diferença pelo valor antigo.
4. Multiplicar por `100` para obter o aumento percentual.
5. Imprimir o resultado com duas casas decimais.

### Fórmula
```text
             valor novo - valor antigo
aumento % = --------------------------- × 100
                     valor antigo
```

## Pseudocodigo
```text
leia valor_antigo, valor_novo

aumento <- (valor_novo - valor_antigo) / valor_antigo * 100

mostre aumento
```