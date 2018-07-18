while True:
	try:
		S = input()
		res = ""

		for k in S:
			o = ord(k)
			if o >= 65 and o <= 90: # A to Z
				o += 13
				if o > 90:
					o = o - 90 + 64
				res += chr(o)
			elif o >= 97 and o <= 122: # a to z
				o += 13
				if o > 122:
					o = o - 122 + 96
				res += chr(o)
			else:
				res += k

		print(res)
	
	except:
		break
