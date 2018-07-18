N,C = map(int,input().split())

P = 0
excedeu = False

for k in range(N):
    S,E = map(int,input().split())
    P += E-S
    if P > C: excedeu = True

print('S') if excedeu else print('N')
