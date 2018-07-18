for k in range(int(input())):
	S = input()

	for w in range(int(input())):
		issub = False
		sub = input()

		it = 0
		subLen = len(sub)
		for l in S:
			if l == sub[it]:
				it += 1

				if it == subLen:
					issub = True
					break

		if issub: print("Yes")
		else: print("No")
