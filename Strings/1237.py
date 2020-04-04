# Time limit exceeded

while True:
	try:
		A = input()
		B = input()

		lA = len(A)
		lB = len(B)

		biggest = ""
		shortest = ""
		lshortest = 0
		if max(lA, lB) == lA:
			biggest, shortest = A, B
			lbiggest = lA
			lshortest = lB
		else:
			biggest, shortest = B, A
			lbiggest = lB
			lshortest = lA


		bSub = 0
		currentSub = 0
		for k in range(lshortest):
			for w in range(lbiggest):
				if shortest[k] == biggest[w]:
					currentSub = 1

					q = w+1

					for p in range(k+1,lshortest):
						if q >= lbiggest:
							break
						if shortest[p] == biggest[q]:
							currentSub += 1
							q += 1
						else:
							break

				if currentSub >= bSub:
					bSub = currentSub

		print(bSub)
	
	except:
		break