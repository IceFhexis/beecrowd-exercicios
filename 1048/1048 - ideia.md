# 1048 - Aumento de salario

## Ideia
Ler 1 numero com ponto flutuante, verificar em qual intervalor esse se encontra e calcular o reajuste

## Passos
- Ler o salario
- Aplicar um reajuste com base no intervalo que se enquadra
- Imprimir: Novo salario, reajuste ganho e percentual

## Pseudocodigo

```text
leia salario


se salario <= 400 entao
    reajuste <- 0.15
se nao
    se salario <= 800 entao
        reajuste <- 0.12
    se nao
        se salario <= 1200 entao
            reajuste <- 0.1
        se nao
            se salario <= 2000 entao
                reajuste <- 0.07
            se nao
                reajuste <- 0.04

novo_salario <- salario * (1 - reajuste)
ganho <- novo_salario - salario 
percentual <- reajuste * 100

mostre "Novo salario:", novo_salario
mostre "Reajuste ganho:", ganho
mostre "Em percentual:", "%", percentual
