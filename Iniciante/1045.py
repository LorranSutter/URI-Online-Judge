nums = map(float, input().split())

A, B, C = sorted(nums, reverse = True)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A*A == B*B + C*C:
        print("TRIANGULO RETANGULO")
    elif A*A > B*B + C*C:
        print("TRIANGULO OBTUSANGULO")
    elif A*A < B*B + C*C:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
