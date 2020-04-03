X = int(input())
Y = int(input())

X,Y = [X,Y] if X < Y else [Y,X]

X += 1 if X%2 == 0 else 2

print(sum(range(X,Y,2)))
