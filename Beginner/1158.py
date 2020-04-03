for k in range(int(input())):
    X,Y = map(int,input().split())
    if X%2 == 0: X+=1
    print(sum([k for k in range(X,X+2*Y,2)]))
