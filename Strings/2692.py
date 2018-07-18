M, N = tuple(map(int,input().split()))

trans = dict()

for k in range(M):
	E,S = tuple(input().split())
	trans[E] = S
	trans[S] = E

keys = trans.keys()

for k in range(N):
	frase = input()
	new_frase = ""
	for letter in frase:
		if letter in keys:
			new_frase += trans[letter]
		else:
			new_frase += letter

	print(new_frase)
