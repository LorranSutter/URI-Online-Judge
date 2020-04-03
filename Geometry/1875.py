for k in range(int(input())):
	R, G, B = 0, 0, 0
	for w in range(int(input())):
		S = input().split()

		if   S[0] == 'R' and S[1] == 'B': R += 1
		elif S[0] == 'R' and S[1] == 'G': R += 2
		elif S[0] == 'G' and S[1] == 'R': G += 1
		elif S[0] == 'G' and S[1] == 'B': G += 2
		elif S[0] == 'B' and S[1] == 'G': B += 1
		elif S[0] == 'B' and S[1] == 'R': B += 2

	if R == G and G == B:
		print("trempate")
	elif R == G and B < G:
		print("empate")
	elif R == B and G < R:
		print("empate")
	elif G == B and R < G:
		print("empate")
	elif max(R,G,B) == R:
		print("red")
	elif max(R,G,B) == B:
		print("blue")
	elif max(R,G,B) == G:
		print("green")

