X = int(input())
Y = int(input())
c = 1
if Y < X: c = -1
print(sum([k for k in range(X,Y+c,c) if k%13 != 0]))
