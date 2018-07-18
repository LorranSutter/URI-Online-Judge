X = int(input())
Z = int(input())

while Z <= X:
    Z = int(input())

k = 1
soma = X
while Z >= soma:
    soma+=X+k
    k+=1

print(k)
