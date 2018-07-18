N = int(input())

while N != 0:
	L1 = list(range(1,N+1))
	L2 = ""

	while len(L1) >= 2:
		L2 += str(L1.pop(0)) + ", "
		L1.append(L1.pop(0))

	print("Discarded cards: " + L2[:-2])
	print("Remaining card: " + str(L1[0]))

	N = int(input())

