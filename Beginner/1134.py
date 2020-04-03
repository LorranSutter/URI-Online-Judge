A = 0
G = 0
D = 0

while True:
    T = int(input())
    if T == 4: break
    if   T == 1: A+=1
    elif T == 2: G+=1
    elif T == 3: D+=1

print("MUITO OBRIGADO")
print("Alcool: %d" % (A))
print("Gasolina: %d" % (G))
print("Diesel: %d" % (D))
