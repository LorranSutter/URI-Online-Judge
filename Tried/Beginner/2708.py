# Wrong answer 20%

jipes = 0
turistas = 0
action = input()

while action != "ABEND":
    if action == "SALIDA":
        jipes += 1
        turistas += int(input())
    elif action == "VUELTA":
        if jipes > 0:
            jipes -= 1
        T = int(input())
        if turistas > 0:
            turistas -= T
    else:
        break

    action = input()

print(turistas)
print(jipes)
