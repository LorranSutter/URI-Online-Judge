Q = int(input())
V = sum(tuple(map(int,input().split())))

if V < Q/2:
	print("Y")
else:
	print("N")