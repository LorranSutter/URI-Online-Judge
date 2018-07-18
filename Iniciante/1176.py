def Fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    a = 0
    b = 1
    c = 1
    for k in range(2,n+1):
        c = a+b
        a = b
        b = c
    return c

for k in range(int(input())):
    N = int(input())
    print("Fib(%d) = %d" % (N,Fib(N)))
