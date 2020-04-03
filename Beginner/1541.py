from math import sqrt

while True:
    S = input()
    if S == '0': break
    A,B,C = map(int,S.split())
    print("%d" % (sqrt(A*B*(100/C))))
