for k in range(int(input())):
	T = input()

	tiros = tuple(map(int,input().split()))
	pulos = input()

	tot = 0
	for t,p in zip(tiros,pulos):
		if p == 'S' and t <= 2:
			tot += 1
		elif p == 'J' and t > 2:
			tot += 1

	print(tot)
