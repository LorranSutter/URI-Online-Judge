notas = [100,50,20,10,5,2]
while True:
    N,M = map(int,input().split())
    if N == M == 0: break
    troco = M-N
    pos = True
    num_notas = 0
    for k in notas:
        num_notas += troco//k
        if num_notas > 2:
            pos = False
            break
        troco = troco%k
    if num_notas <= 1: pos = False
    print("possible") if pos else print("impossible")
