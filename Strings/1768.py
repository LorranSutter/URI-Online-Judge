while True:
	try:
		N = int(input())
		rate = N//2

		for k,it in zip(range(rate,-1,-1), range(1,N+1,2)):
			print(k * ' ' + it * '*')

		print(rate * ' ' + '*')
		print((rate-1) * ' ' + '***')
		print()

	except:
		break
