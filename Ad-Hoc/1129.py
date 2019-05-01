N = int(input())

while N != 0:
	for k in range(N):
		resp = ""
		it = 65
		for w in tuple(map(int,input().split())):
			if w <= 127:
				if resp == "":
					resp = chr(it)
				else:
					resp = '*'
					break
			it += 1
		if resp == "": resp = '*'
		print(resp)

	N = int(input())
