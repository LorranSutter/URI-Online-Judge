# Runtime Error

for k in range(int(input())):
	input()
	L = sorted(list(map(int,input().split()))) # Memory problem
	res = ""
	for k in L:
		res += str(k) + ' '
	print(res[:-1])