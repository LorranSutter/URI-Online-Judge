while True:
	try:
		A, B = tuple(map(int,input().split()))
		A, B = bin(A)[2:], bin(B)[2:]

		lA = len(A)
		lB = len(B)
		if lB > lA:
			A = (lB-lA)*'0' + A
		else:
			B = (lA-lB)*'0' + B

		res = ''
		for k in range(max(lA,lB)):
			if   A[k] == '0' and B[k] == '1': res += '1'
			elif A[k] == '1' and B[k] == '0': res += '1'
			else: res += '0'

		print(int(res,2))
	
	except:
		break
