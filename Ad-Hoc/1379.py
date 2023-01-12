while True:
    A,B = input().split()
    if A == '0' and B == '0':
        break
    A, B = int(A), int(B)
    print(2*A-B)
