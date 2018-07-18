C = 0
R = 0
S = 0
for k in range(int(input())):
    Q, T = input().split()
    if   T == 'C': C+=int(Q)
    elif T == 'R': R+=int(Q)
    else:          S+=int(Q)

tot = C+R+S

print("Total: %d cobaias" % (tot))
print("Total de coelhos: %d" % (C))
print("Total de ratos: %d" % (R))
print("Total de sapos: %d" % (S))
print("Percentual de coelhos: %.2f %%" % (100*C/tot))
print("Percentual de ratos: %.2f %%" % (100*R/tot))
print("Percentual de sapos: %.2f %%" % (100*S/tot))
