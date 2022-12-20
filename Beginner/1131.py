gremio, inter, draw, matches = 0, 0, 0, 0
while True:
    matches += 1
    i, g = map(int,input().split())
    if g > i: gremio += 1
    elif g < i: inter += 1
    else: draw += 1

    new = input("Novo grenal (1-sim 2-nao)\n")
    if new == "2": break

print("{} grenais".format(matches))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(draw))

if gremio > inter: print("Gremio venceu mais")
elif gremio < inter: print("Inter venceu mais")
else: print("Nao houve vencedor")
