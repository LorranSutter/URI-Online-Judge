import math

N = int(input())

for k in range(N):
	C = float(input())
	D = math.log2(C)
	
	print(str(math.ceil(D)) + " dias")
