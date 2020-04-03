for k in range(int(input())):
	H, M, O = input().split()

	H = '0' + H if len(H) == 1 else H
	M = '0' + M if len(M) == 1 else M

	print("{0}:{1} - A porta {2}!".format(H,M,"abriu" if O == "1" else "fechou"))
