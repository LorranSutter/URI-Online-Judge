N,M = map(int,input().split())
for k in range(M):
    N += 1 if input() == "fechou" else -1
print(N)
