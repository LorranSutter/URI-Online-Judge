p1 = p2 = 0
while True:
    N = int(input())
    if N == 0: break
    for k in range(N):
        A, B = map(int,input().split())
        if   A > B: p1+=1
        elif B > A: p2+=1
    print("%d %d" % (p1,p2))
    p1 = p2 = 0
