# 2162 - Picos e Vales

## Ideia

Comparar cada medida com a anterior para descobrir se é um pico ou um vale. A sequência é válida somente se essas comparações alternarem entre maior e menor, sem valores iguais consecutivos.

## Passos

Ler a quantidade de medidas N.
Guardar as N alturas da paisagem.
Percorrer as medidas a partir da segunda, comparando cada uma com a anterior.
Se duas medidas consecutivas forem iguais, o padrão é inválido.
Verificar se a comparação atual (> ou <) é diferente da comparação anterior.
Se duas comparações consecutivas forem iguais, o padrão é inválido.
Se nenhuma condição inválida for encontrada, imprimir 1; caso contrário, imprimir 0.