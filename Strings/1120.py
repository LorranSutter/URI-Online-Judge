while True:
    D,N = input().split()
    if D == N == '0': break
    N = N.replace(D,'')
    print(0) if N == '' else print(int(N))
