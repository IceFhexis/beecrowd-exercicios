# 2003 - Domingo

## Ideia
O horario informado indica quando a pessoa acordou. O pior caso leva 60 minutos para chegar ao terminal, que fecha as 8:00. Calcular o atraso comparando a chegada com 8:00.

## Passos
1. Ler horas e minutos no formato `H:MM`.
2. Converter o horario para minutos desde meia-noite.
3. Somar 60 minutos para obter a chegada.
4. Comparar com 8 * 60.
5. Se chegar antes ou exatamente as 8:00, o atraso é zero; caso contrario, subtrair os horarios.
6. Repetir ate o fim da entrada.
