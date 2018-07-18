def ehPerfeito(n):
    if n == 1: return False
    soma = 1
    for k in range(2,n):
        if n%k == 0: soma+=k
    return n == soma

for k in range(int(input())):
    N = int(input())
    if ehPerfeito(N):
        print("%d eh perfeito" % (N))
    else:
        print("%d nao eh perfeito" % (N))
