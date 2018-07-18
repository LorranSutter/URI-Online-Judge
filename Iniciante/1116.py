for k in range(int(input())):
    a, b = map(float,input().split())
    if b == 0: print("divisao impossivel")
    else: print("%.1f" % (a/b))
