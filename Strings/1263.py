while True:
	try:
		S = input().split()

		last = S[0][0].lower()
		letter = S[0][0].lower()
		found = False
		res = 0

		for k in S[1:]:
			l = k[0].lower()
			if l == letter and not found:
				found = True
				res += 1
			elif last != l:
				last = l
				found = False
				letter = l

		print(res)

	except:
		break
