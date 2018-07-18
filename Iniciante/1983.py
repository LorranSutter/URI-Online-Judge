mat = ''
nota = -1
for k in range(int(input())):
    X,Y = input().split()
    Y = float(Y)
    if Y > nota:
         mat = X
         nota = Y
if nota >= 8:
    print(mat)
else:
    print("Minimum note not reached")
