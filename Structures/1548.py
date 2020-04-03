N = int(input())

for k in range(N):
	M = int(input())
	P = list(map(int,input().split()))
	Psort = sorted(P, reverse = True)

	res = 0
	for w in range(len(P)):
		if P[w] == Psort[w]: res+=1

	print(res)
