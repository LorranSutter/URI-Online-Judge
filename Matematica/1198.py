while True:
	try:
		A, B = tuple(map(int,input().split()))
		print(abs(A-B))

	except:
		break
