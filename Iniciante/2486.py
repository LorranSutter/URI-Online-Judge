T = int(input())

while T != 0:
	tot = 0
	for k in range(T):
		S = input().split()
		N = int(S[0])
		A = ' '.join(S[1:])

		if A == "suco de laranja":
			tot += N*120
		elif A == "morango fresco":
			tot += N*85
		elif A == "mamao":
			tot += N*85
		elif A == "goiaba vermelha":
			tot += N*70
		elif A == "manga":
			tot += N*56
		elif A == "laranja":
			tot += N*50
		elif A == "brocolis":
			tot += N*34

	if tot < 110:
		print("Mais {0} mg".format(110-tot))
	elif tot > 130:
		print("Menos {0} mg".format(tot-130))
	else:
		print("{0} mg".format(tot))

	T = int(input())
