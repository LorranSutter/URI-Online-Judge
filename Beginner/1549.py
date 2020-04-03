from math import pi

heightVol = lambda V, B, b: 3*V/((B*B + B*b + b*b)*pi)

for k in range(int(input())):
    N, L = map(int, input().split())
    b, B, H = map(int, input().split())

    print(round(heightVol(L/N, B, b), 2))
