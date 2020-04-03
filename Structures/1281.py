for k in range(int(input())):
	d = dict()
	for w in range(int(input())):
		S = input().split()
		d[S[0]] = float(S[1])

	keys = d.keys()
	total = 0
	for w in range(int(input())):
		S = input().split()
		if S[0] in keys:
			total += int(S[1]) * d[S[0]]

	print("R$ {:.2f}".format(total))
