while True:
	try:
		N, M = input().split()

		one = tuple()
		two = tuple()

		for k in range(int(N)):
			S = input().split()
			for w in range(int(M)):
				if S[w] == '1':
					one = (k,w)
				elif S[w] == '2':
					two = (k,w)

		print(abs(one[0]-two[0]) + abs(one[1]-two[1]))

	except:
		break
