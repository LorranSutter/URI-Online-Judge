S = input().split()

while S[0] != '0':
	Q, D, P = tuple(map(int,S))
	T = int(Q*D*P/(P-Q))

	if T == 1:
		print("1 pagina")
	else:
		print("{0:d} paginas".format(T))

	S = input().split()
