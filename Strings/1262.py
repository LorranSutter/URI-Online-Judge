while True:
	try:
		S = input()
		P = int(input())
		cicles = 0

		it = 0
		for k in S:
			if k == 'R':
				it += 1
			elif k == 'W':
				if it > 0: cicles += 1
				it = 0
				cicles += 1
			if it == P:
				it = 0
				cicles += 1

		if it > 0:
			cicles += 1

		print(cicles)
	
	except:
		break
