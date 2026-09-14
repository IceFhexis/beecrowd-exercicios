# 1019 - Conversão de Tempo

## Ideia
Ler um tempo em segundos e converter esse valor para horas, minutos e segundos.

Primeiro descobrimos quantas horas completas existem. Depois, usamos o tempo restante para calcular os minutos e os segundos.

## Passos
1. Ler o tempo total em segundos.
2. Dividir o tempo por `3600` para descobrir as horas.
3. Pegar o resto da divisão por `3600`.
4. Dividir o restante por `60` para descobrir os minutos.
5. O resto da divisão por `60` representa os segundos.
6. Imprimir no formato `horas:minutos:segundos`.

## Pseudocodigo
```text
leia tempo

horas <- tempo // 3600
resto <- tempo % 3600

minutos <- resto // 60
segundos <- resto % 60

mostre horas:minutos:segundos
```