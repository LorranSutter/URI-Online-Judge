N = int(input())

if N%2 == 0: N += 1

for k in range(2,N,2):
    print("%d^2 = %d" % (k,k**2))
