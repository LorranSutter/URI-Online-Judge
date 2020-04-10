A, B = map(int, input().split())

while A != 0 and B != 0:
    X = set(map(int, input().split()))
    Y = set(map(int, input().split()))

    print(min(len(X-Y), len(Y-X)))

    A, B = map(int, input().split())
