for k in range(int(input())):
	diet = list(set(k for k in input()))
	breakfast = [k for k in input()]
	lunch = [k for k in input()]

	ate = breakfast + lunch

	miss = []

	for food in diet:
		try:
			ate.remove(food)
		except:
			miss.append(food)

	if ate != []:
		print("CHEATER")
	else:
		print(''.join(sorted(miss)))
