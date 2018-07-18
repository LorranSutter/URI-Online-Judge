for k in range(int(input())):
	Hash = 0
	for w in range(int(input())):
		L = input()
		for l in range(len(L)):
			Hash += ord(L[l])-65 + w + l
	print(Hash)
