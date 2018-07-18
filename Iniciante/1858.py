N = int(input())
T = list(map(int,input().split()))

menor = T[0]
pos = 1

for k in range(1,N):
    if T[k] < menor:
        menor = T[k]
        pos = k+1

print(pos)
