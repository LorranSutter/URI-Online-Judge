# Timelimit exeeded

M = [[0 for _ in range(501)] for _ in range(501)]

for _ in range(int(input())):
    S = input().split()

    if S[0] == 'U':
        X, Y, Z, W, V = tuple(map(int, S[1:]))

        for i in range(X-1, Z):
            for j in range(Y-1, W):
                M[i][j] += V

    else:
        print(M[int(S[1])-1][int(S[2])-1])
