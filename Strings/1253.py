for k in range(int(input())):
	S = input()
	num = int(input())
	res = ""

	for k in S:
		l = ord(k) - num

		if l < 65:
			l = 90 - (64 - l)

		res += chr(l)

	print(res)
