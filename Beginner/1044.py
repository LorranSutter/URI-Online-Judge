A, B = map(float, input().split())

if (A > B and A % B == 0) or (B >= A and B % A == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
