N = input()

while N != '-1':
	if N[:2] == '0x':
		print(int(N[2:],16))
	else:
		N = hex(int(N))
		print(N[:2] + N[2:].upper())

	N = input()
