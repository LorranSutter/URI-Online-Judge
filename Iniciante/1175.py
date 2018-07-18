N = [0 for k in range(20)]
for k in range(20):
    N[k] = int(input())

for k,w in enumerate(N):
    if w: print("N[%d] = %d" % (k,N[19-k]))
