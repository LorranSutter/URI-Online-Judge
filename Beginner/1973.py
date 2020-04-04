# Runtime error

N = int(input())
X = list(map(int, input().split())) # Memory problem
tot = sum(X)

visited = [False for k in range(N)]

currentStar = 0
while True:
    if currentStar < 0 or currentStar > N-1:
        break
    else:
        visited[currentStar] = True
        if X[currentStar] >= 1:
            if X[currentStar] % 2 == 0:
                X[currentStar] -= 1
                currentStar -= 1
            else:
                X[currentStar] -= 1
                currentStar += 1
            tot -= 1
        else:
            if X[currentStar] % 2 == 0:
                currentStar -= 1
            else:
                currentStar += 1

print("{0} {1}".format(sum(visited), tot))
