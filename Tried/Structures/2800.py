# Time limit exeeded

while True:
    try:
        N, Q = map(int, input().split())
        X = list(map(int, input().split()))

        for k in range(Q):
            C = list(map(int, input().split()))
            if C[0] == 1:
                X[C[1] - 1] = C[2]
            else:
                s = 0
                for w in X[C[1]-1:C[2]]:
                    if w != C[3]:
                        s += 1
                print(s)
    except:
        break
