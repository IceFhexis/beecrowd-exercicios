# 2057 - Fuso Horario

## Ideia
A hora de chegada e a soma da hora de saida, do tempo de viagem e do deslocamento de fuso. Como o relogio tem 24 horas, ajustar o resultado para ficar entre 0 e 23.

## Passos
1. Ler `S`, `T` e `F`.
2. Calcular `S + T + F`.
3. Se o resultado passar de 23, voltar 24 horas.
4. Se ficar negativo, avancar 24 horas.
5. Imprimir a hora ajustada.
