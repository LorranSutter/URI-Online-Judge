for k in range(int(input())):
	S = input().split()
	N = sum(tuple(map(int,input().split())))

	if S[1] == "PAR":
		if N % 2 == 0:
			print(S[0])
		else:
			print(S[2])
	else:
		if N % 2 == 0:
			print(S[2])
		else:
			print(S[0])
