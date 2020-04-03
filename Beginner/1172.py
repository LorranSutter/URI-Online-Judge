X = [0 for k in range(10)]
for k in range(10):
    n = int(input())
    if n <= 0: X[k] = 1
    else: X[k] = n

for k,w in enumerate(X):
    print("X[%d] = %d" % (k,w))
