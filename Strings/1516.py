N, M = tuple(map(int,input().split()))

while N != 0 and M != 0:
	S = ["" for k in range(N)]
	for k in range(N):
		S[k] = input()
	A, B = tuple(map(int,input().split()))
	rateLines = A // N
	rateColumns = B // M

	for k in S:
		line = ""
		for w in k:
			line += rateColumns*w
		for w in range(rateLines):
			print(line)

	print()
	N, M = tuple(map(int,input().split()))
