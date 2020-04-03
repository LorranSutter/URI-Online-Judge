A = [0 for k in range(100)]
T = [False for k in range(100)]
for k in range(100):
    A[k] = float(input())
    if A[k] <= 10: T[k] = True

for k,w in enumerate(T):
    if w: print("A[%d] = %.1f" % (k,A[k]))
