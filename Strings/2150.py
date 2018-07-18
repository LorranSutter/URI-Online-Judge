while True:
	try:
		S = input()

		count = 0
		for k in input():
			if k in S:
				count += 1

		print(count)

	except:
		break
