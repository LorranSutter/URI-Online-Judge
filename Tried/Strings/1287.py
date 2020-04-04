# Wrong answer 100%

while True:
	try:
		S = input()

		if S == "":
			print("error")
		else:
			res = ""
			for k in S:
				if k.isnumeric(): res += k
				elif k == 'o' or k == 'O': res += '0'
				elif k == 'l': res += '1'
				elif k == ',' or k == ' ': continue
				else:
					res = 'error'
					break

			if res == 'error':
				print(res)
			elif int(res) > 2147483647:
				print('error')
			else:
				print(int(res))

	except:
		break