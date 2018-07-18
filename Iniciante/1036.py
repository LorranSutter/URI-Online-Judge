from math import sqrt
a, b, c = map(float,input().split())
if a <= 0:
    print("Impossivel calcular")
else:
    delta = b*b-4*a*c
    if delta < 0:
        print("Impossivel calcular")
    else:
        print("R1 = %.5f" % ((-b+sqrt(delta))/(2*a)))
        print("R2 = %.5f" % ((-b-sqrt(delta))/(2*a)))
