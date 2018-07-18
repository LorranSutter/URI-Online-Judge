while True:
	try:
		N = int(input())

		for k in range(N):
			line = ""
			for w in range(N):
				if abs(k+w) == N-1:
					line += "2"
				elif k == w:
					line += "1"
				else:
					line += "3"
			print(line)
	except:
		break
