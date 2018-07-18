while True:
	try:
		res = ''
		sub = False
		ast = False
		for char in input():
			if char == '_':
				if sub:
					res += "</i>"
					sub = False
				else:
					res += "<i>"
					sub = True
			elif char == '*':
				if ast:
					res += "</b>"
					ast = False
				else:
					res += "<b>"
					ast = True
			else:
				res += char

		print(res)

	except:
		break
