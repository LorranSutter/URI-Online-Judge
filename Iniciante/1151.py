N = int(input())

if N == 1: print(0)
elif N == 2: print("0 1")
else:
    a = 0
    b = 1
    c = 0
    res = "0 1 "
    for k in range(2,N):
        c = a+b
        res += str(c) + " "
        a = b
        b = c
    print(res[:-1])
