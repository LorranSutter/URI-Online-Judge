while True:
	try:
		writeBegin = False
		begin = ""
		res = ""

		for k in input():
			if k == "[":
				writeBegin = True
				res = begin + res
				begin = ""
			elif k == "]":
				writeBegin = False
				res = begin + res
				begin = ""
			elif writeBegin:
				begin += k
			else:
				res += k

		if begin != "":
			res = begin + res

		print(res)

	except:
		break
