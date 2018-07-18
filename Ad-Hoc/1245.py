while True:
	try:
		esquerdos = [0 for k in range(31)]
		direitos = [0 for k in range(31)]

		for k in range(int(input())):
			M, L = input().split()

			if L == 'E':
				esquerdos[int(M)-30] += 1
			else:
				direitos[int(M)-30] += 1

		tot = 0
		for e,d in zip(esquerdos,direitos):
			tot += min(e,d)

		print(tot)

	except:
		break
