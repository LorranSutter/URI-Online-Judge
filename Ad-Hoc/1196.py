while True:
	try:
		S = input()
		res = ""

		for k in S:	
			if   k == '1': res += '`'
			elif k == '2': res += '1'
			elif k == '3': res += '2'
			elif k == '4': res += '3'
			elif k == '5': res += '4'
			elif k == '6': res += '5'
			elif k == '7': res += '6'
			elif k == '8': res += '7'
			elif k == '9': res += '8'
			elif k == '0': res += '9'
			elif k == '-': res += '0'
			elif k == '=': res += '-'

			elif k == 'W': res += 'Q'
			elif k == 'E': res += 'W'
			elif k == 'R': res += 'E'
			elif k == 'T': res += 'R'
			elif k == 'Y': res += 'T'
			elif k == 'U': res += 'Y'
			elif k == 'I': res += 'U'
			elif k == 'O': res += 'I'
			elif k == 'P': res += 'O'
			elif k == '[': res += 'P'
			elif k == ']': res += '['
			elif k == '\\': res += ']'

			elif k == 'S': res += 'A'
			elif k == 'D': res += 'S'
			elif k == 'F': res += 'D'
			elif k == 'G': res += 'F'
			elif k == 'H': res += 'G'
			elif k == 'J': res += 'H'
			elif k == 'K': res += 'J'
			elif k == 'L': res += 'K'
			elif k == ';': res += 'L'
			elif k == '\'': res += ';'

			elif k == 'X': res += 'Z'
			elif k == 'C': res += 'X'
			elif k == 'V': res += 'C'
			elif k == 'B': res += 'V'
			elif k == 'N': res += 'B'
			elif k == 'M': res += 'N'
			elif k == ',': res += 'M'
			elif k == '.': res += ','
			elif k == '/': res += '.'

			else: res += ' '

		print(res)

	except:
		break
