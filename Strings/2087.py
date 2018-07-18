while True:
    N = int(input())
    if N == 0: break
    P = [input() for k in range(N)]
    
    ruim = False
    l_p = len(P)
    for k in range(l_p):
        l = len(P[k])
        for w in range(l_p):
            if k != w and l <= len(P[w]):
                if P[k] == P[w][:l]:
                    ruim = True
                    break
        if ruim: break
    if ruim:
        print("Conjunto Ruim")
    else:
        print("Conjunto Bom")
