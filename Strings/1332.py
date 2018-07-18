for k in range(int(input())):
	S = input()

	if len(S) == 5:
		print(3)
	else:
		if ((S[0] == "o") + (S[1] == "n") + (S[2] == "e")) >= 2: print(1)
		else: print(2)
