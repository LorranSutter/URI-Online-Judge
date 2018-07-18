N = int(input())
L = ['' for k in range(N)]
n = 0
for k in range(N):
    S = input()
    contem = False
    for w in range(n+1):
        if S == L[w]:
            contem = True
            break
    if not contem:
        L[n] = S
        n+=1

print("Falta(m) %d pomekon(s)." % (151-n))
