T = int(input())
w = 0
for k in range(1000):
    print("N[%d] = %d" % (k,w))
    w+=1
    if w == T: w = 0
