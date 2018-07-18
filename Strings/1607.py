for k in range(int(input())):
	A, B = input().split()
	res = 0

	for w in range(len(A)):
		num = ord(B[w]) - ord(A[w])
		if num < 0:
			res += 26
		res += num

	print(res)
