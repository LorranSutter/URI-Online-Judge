for k in range(int(input())):
	N, M = tuple(map(int,input().split()))

	trips = 1
	charge = 0
	for w in input().split():
		w = int(w)
		if charge + w > M:
			trips += 1
			charge = w
		else:
			charge += w

	print(trips)
