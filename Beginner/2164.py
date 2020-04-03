from math import sqrt

N = int(input())

r_5 = sqrt(5)

print("%.1f" % (( ((1+r_5)/2)**N - ((1-r_5)/2)**N )/r_5))
