# 1957 - Converter para Hexadecimal

## Ideia
Converter um número da base 10 (decimal) para a base 16 (hexadecimal).

No hexadecimal existem 16 símbolos:

0 1 2 3 4 5 6 7 8 9 A B C D E F

Para fazer a conversão manualmente, dividimos o número por 16 várias vezes e guardamos o resto de cada divisão.

Os restos formam o número hexadecimal, mas aparecem de trás para frente.

## Passos
1. Ler o número inteiro V.
2. Criar uma string vazia para guardar o hexadecimal.
3. Enquanto V for maior que 0:  
    Calcular o resto da divisão de V por 16.
    Converter esse resto para o símbolo hexadecimal correspondente.
    Adicionar o símbolo no início da resposta.
    Dividir V por 16 usando divisão inteira.
4. Imprimir o número hexadecimal.

## Pseudocodigo

```text
Ler V

Criar hexadecimal vazio

Enquanto V for maior que 0:
    resto = V % 16

    Se resto for menor que 10:
        converter resto para "0" até "9"
    Senão:
        converter resto para "A" até "F"

    adicionar o símbolo no início de hexadecimal

    V = V dividido por 16

Imprimir hexadecimal
```