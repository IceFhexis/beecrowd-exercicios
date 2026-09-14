inter = 0
gremio = 0
empates = 0
grenais = 0

while True:
    gols_inter, gols_gremio = map(int, input().split())
    grenais += 1

    if gols_inter > gols_gremio:
        inter += 1
    elif gols_gremio > gols_inter:
        gremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    if int(input()) == 2:
        break

print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empates}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")