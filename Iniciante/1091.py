K = int(input())

while K != 0:
	N, M = tuple(map(int,input().split()))

	for k in range(K):
		X, Y = tuple(map(int,input().split()))

		if   X == N or Y == M: print("divisa")
		elif X > N  and Y > M: print("NE")
		elif X < N  and Y > M: print("NO")
		elif X > N  and Y < M: print("SE")
		elif X < N  and Y < M: print("SO")

	K = int(input())
