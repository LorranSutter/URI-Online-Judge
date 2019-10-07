A, B, C = map(float, input().split())

if not(abs(A - B) < C < A + B):
    print("Area = {0:0.1f}".format((A+B)*C/2))
elif not(abs(A - C) < B < A + C):
    print("Area = {0:0.1f}".format((A+B)*C/2))
elif not(abs(B - C) < A < B + C):
    print("Area = {0:0.1f}".format((A+B)*C/2))
else:
    print("Perimetro = {0:0.1f}".format(A+B+C))
