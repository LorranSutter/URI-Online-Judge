for k in range(int(input())):
    X,Y = map(int,input().split())
    if Y < X:
        a = X
        X = Y
        Y = a
    if X%2 != 0: X+=1
    print(sum([k for k in range(X+1,Y,2)]))
