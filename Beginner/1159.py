while True:
    X = int(input())
    if X == 0: break
    if X%2 != 0: X+=1
    print(sum([k for k in range(X,X+10,2)]))
