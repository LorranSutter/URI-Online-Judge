while True:
	try:
		N = int(input())
		L = ["" for k in range(N)]

		for k in range(N):
			L[k] = input()

		for k in sorted(L):
			print(k)

	except:
		break
