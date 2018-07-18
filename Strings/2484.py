while True:
	try:
		S = input()
		l = len(S)

		for k in range(l,0,-1):
			print(' ' * (l - k) + ' '.join(S[:k]))

		print()

	except:
		break
