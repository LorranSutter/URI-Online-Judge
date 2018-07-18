while True:
	A, B = input().split()

	if A == '0' and B == '0':
		break

	lA, lB = len(A), len(B)
	if lA > lB:
		bigger = lA
	else:
		bigger = lB

	A, B = int(A), int(B)

	carry = 0
	nextOp = 0	
	for k in range(bigger):
		s = A%10 + B%10 + nextOp
		if s >= 10:
			nextOp = 1
			carry += 1
		else:
			nextOp = 0

		A = A//10
		B = B//10

	if carry == 0:
		print("No carry operation.")
	elif carry == 1:
		print("1 carry operation.")
	else:
		print("{0} carry operations.".format(carry))	
