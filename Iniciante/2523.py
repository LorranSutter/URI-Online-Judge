while True:
	try:
		S = input()
		N = input()
		print(''.join([S[int(k)-1] for k in input().split()]))

	except:
		break
