while True:
	try:
		S = input()

		l = len(S)
		if l < 6 or l > 32:
			print("Senha invalida.")
		else:
			M = False
			m = False
			num = False
			valida = True
			for k in S:
				if k == " ":
					valida = False
					break
				else:
					o = ord(k)

					if   o >= 48 and o <= 57: num = True
					elif o >= 65 and o <= 90: M = True
					elif o >= 97 and o <= 122: m = True
					else:
						valida = False
						break
			if valida and M and m and num:
				print("Senha valida.")
			else:
				print("Senha invalida.")
	except:
		break
