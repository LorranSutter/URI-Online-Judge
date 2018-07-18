for k in range(int(input())):
	L = [(w,len(w)) for w in input().split()]

	L = sorted(L, key=lambda x:x[1], reverse = True)
	L = [w[0] for w in L]

	print(' '.join(L))
