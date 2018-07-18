while True:
	try:
		opened = 0
		closed = 0
		correct = True

		for k in input():
			if k == "(":
				opened += 1
			elif k == ")":
				if opened <= closed:
					correct = False
					break
				else:
					closed += 1

		if not correct:
			print("incorrect")
		elif opened == closed:
			print("correct")
		else:
			print("incorrect")

	except:
		break
