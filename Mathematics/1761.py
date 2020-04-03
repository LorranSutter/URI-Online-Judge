from math import tan, radians

while True:
    try:
        A, B, C = map(float, input().split())
        print("{0:0.2f}".format((tan(radians(A))*B+C)*5))
    except:
        break
