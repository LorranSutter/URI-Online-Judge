for k in range(int(input())):
	alpha = [0 for w in range(26)]

	for w in input():
		o = ord(w)

		if o >= 97 and o <= 122:
			alpha[o-123] = 1

	if sum(alpha) == 26:
		print("frase completa")
	elif sum(alpha) >= 13:
		print("frase quase completa")
	else:
		print("frase mal elaborada")
