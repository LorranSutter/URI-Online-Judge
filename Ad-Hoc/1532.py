# 40% de erro ainda

while True:
    N,V = map(int,input().split())
    if N == V == 0: break

    possivel = False
    it = 0
    n = 0
    while it <= N and V != 0:
        print(it,n,V)
        if N == it:
            possivel = True
            break
        if n == V:
            n = 1
            V -= 1
        else:
            n += 1
        it+=V
    if possivel: print("possivel")
    else: print("impossivel")
