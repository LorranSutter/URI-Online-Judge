def raiz(N):
	if N == 0:
		return 0
	else:
		return 1/(2 + raiz(N-1))

print("{0:.10f}".format(1+raiz(int(input()))))
