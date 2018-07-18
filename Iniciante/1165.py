from math import sqrt

def ehprimo(n):
    if n == 2: return True
    if n == 1 or n%2 == 0: return False
    for k in range(3,int(sqrt(n))+1,2):
        if n%k == 0: return False
    return True

for k in range(int(input())):
    X = int(input())
    if ehprimo(X): print("%d eh primo" % (X))
    else:          print("%d nao eh primo" % (X))
    
