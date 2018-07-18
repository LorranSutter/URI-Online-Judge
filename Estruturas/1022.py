def mdc(m,n):
    if n==0: return m
    return mdc(n,m%n)

for k in range(int(input())):
    A = input().split()
    op = A[3]
    A[0] = int(A[0])
    A[1] = int(A[2])
    A[2] = int(A[4])
    A[3] = int(A[6])
    res = [[],[]]
    if op == '+':
        res[0] = A[0]*A[3]+A[2]*A[1]
        res[1] = A[1]*A[3]
    elif op == '-':
        res[0] = A[0]*A[3]-A[2]*A[1]
        res[1] = A[1]*A[3]
    elif op == '*':
        res[0] = A[0]*A[2]
        res[1] = A[1]*A[3]
    else:
        res[0] = A[0]*A[3]
        res[1] = A[2]*A[1]
    m = mdc(res[0],res[1])
    print("%d/%d = %d/%d" % (res[0],res[1],res[0]/m,res[1]/m))
