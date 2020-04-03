X = int(input())
Y = int(input())

if X > Y:
    aux = X
    X = Y
    Y = aux

for k in range(X+1,Y):
    if k%5 == 2 or k%5 == 3: print(k)
