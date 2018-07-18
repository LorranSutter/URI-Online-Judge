prim = True
while True:
    N = int(input())
    if N == 0: break
    S = ['' for k in range(N)]
    maior = 1
    for k in range(N):
        s = input()
        S[k] = s
        l = len(s)
        if l > maior: maior = l
    if not prim: print("")
    else: prim = False
    for k in S:
        l = len(k)
        if l < maior: print(' '*(maior-l)+k)
        else: print(k)
