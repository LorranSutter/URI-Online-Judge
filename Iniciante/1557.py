while True:
    N = int(input())
    if N == 0: break
    T = ''
    for k in range(len(str(2**(N+N-2)))): T += ' '
    for k in range(N):
        res = ''
        for w in range(N):
            n = str(2**(k+w))
            res += T[:-(len(n))] + n + ' '
        print(res[:-1])
    print("")
