N, M = tuple(map(int,input().split()))

while N != 0 and M != 0:
	originais = [0 for k in range(N)]

	for k in tuple(map(int,input().split())):
		originais[k-1] += 1

	tot = 0
	for k in originais:
		if k > 1:
			tot += 1

	print(tot)

	N, M = tuple(map(int,input().split()))
