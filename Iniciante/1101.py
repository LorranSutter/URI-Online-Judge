while True:
    M,N = map(int,input().split())
    if M <= 0 or N <= 0: break
    if N < M:
        a = M
        M = N
        N = a
    res = ''
    soma = 0
    for k in range(M,N+1):
        res+=str(k)+' '
        soma+=k
    print(res + "Sum=" + str(soma))
