N = int(input())
X = list(map(int,input().split()))

menor = X[0]
pos = 0

for k in range(1,N):
    if X[k] < menor:
        menor = X[k]
        pos = k

print("Menor valor: %d" % (menor))
print("Posicao: %d" % (pos))
