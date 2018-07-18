N = int(input())

soma = 0

for k in range(N):
    X = int(input())
    if X >= 10 and X <= 20: soma+=1

print("%d in" % (soma))
print("%d out" % (abs(N-soma)))
