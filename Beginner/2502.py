while True:
	try:
		C, N = tuple(map(int,input().split()))
		C1, C2 = input(), input()

		crypt = dict()

		for k in range(C):
			if C1[k] not in crypt.keys():
				if C1[k].isalpha() and C2[k].isalpha():
					crypt[C1[k].lower()] = C2[k].lower()
					crypt[C2[k].lower()] = C1[k].lower()
				elif C1[k].isalpha():
					crypt[C1[k].lower()] = C2[k]
					crypt[C2[k]] = C1[k].lower()
				elif C2[k].isalpha():
					crypt[C1[k]] = C2[k].lower()
					crypt[C2[k].lower()] = C1[k]
				else:
					crypt[C1[k]] = C2[k]
					crypt[C2[k]] = C1[k]
		
		for k in range(N):
			res = ""
			S = input()
			for letter in S:
				if letter.isalpha():
					lowerLetter = letter.lower()
					if lowerLetter in crypt.keys():
						if letter.islower():
							res += crypt[letter]
						else:
							res += crypt[lowerLetter].upper()
					else:
						res += letter
				elif letter in crypt.keys():
					res += crypt[letter]
				else:
					res += letter

			print(res)

		print()
	
	except:
		break
