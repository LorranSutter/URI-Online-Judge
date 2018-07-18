N, W = tuple(map(int,input().split()))

for k in range(N):
	S = input()

	H = ""
	name = ""
	for w in range(len(S)-1,-1,-1):
		if S[w] == ' ':
			H = int(H[::-1])
			name = S[:w]
			break
		else:
			H += S[w]

	if H > W:
		print(name)
