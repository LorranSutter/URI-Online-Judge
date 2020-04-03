for k in range(int(input())):
	fail = False
	S = input()

	if len(S) != 8:
		print("FAILURE")
	elif '-' not in S:
		print("FAILURE")
	else:
		S = S.split('-')

		for w in S[0]:
			if ord(w) < 65 or ord(w) > 90:
				print("FAILURE")
				fail = True
				break
		if fail: continue

		for w in S[1]:
			if ord(w) < 48 or ord(w) > 57:
				print("FAILURE")
				fail = True
				break
		if fail: continue

		num = int(S[1][-1])
		if   num == 1 or num == 2: print("MONDAY")
		elif num == 3 or num == 4: print("TUESDAY")
		elif num == 5 or num == 6: print("WEDNESDAY")
		elif num == 7 or num == 8: print("THURSDAY")
		elif num == 9 or num == 0: print("FRIDAY")
		else: print("FAILURE")
