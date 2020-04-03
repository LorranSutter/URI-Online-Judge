P1, C1, P2, C2 = map(int,input().split())

left, right = P1*C1, P2*C2

if left == right: print(0)
elif left > right: print(-1)
else: print(1)