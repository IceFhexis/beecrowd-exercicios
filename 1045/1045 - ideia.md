# 1045 - Tipos de Triangulos

## Ideia
Ordenar os tres lados para deixar o maior valor em `A`. Assim, a classificacao dos angulos pode ser feita comparando `A^2` com `B^2 + C^2`.

## Passos
1. Ler os tres lados.
2. Colocar o maior lado em `A`.
3. Se `A >= B + C`, nao existe triangulo.
4. Caso exista, classificar o angulo:
   - igual: retangulo;
   - maior: obtusangulo;
   - menor: acutangulo.
5. Comparar os lados para classificar como equilatero, isosceles ou escaleno.
