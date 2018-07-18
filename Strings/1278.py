N = int(input())

while True:
	S = [[] for k in range(N)]
	S_len = [0 for k in range(N)]
	bigger_len = 0

	for k in range(N):
		S[k] = input().split()
		S_len[k] = sum([len(w) for w in S[k]]) + len(S[k]) - 1

		if S_len[k] > bigger_len:
			bigger_len = S_len[k]

	for k in range(N):
		print(' ' * (bigger_len - S_len[k]) + ' '.join(S[k]))

	N = int(input())

	if N == 0:
		break
	print()
