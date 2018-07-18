while True:
    M, N = map(int, input().split())
    if M == N == 0: break
    res = ''
    for k in str(N+M):
        if k != '0': res+=k
    print(res)
