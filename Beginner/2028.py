count = 1
while True:
	try:
		N = int(input())

		if N == 0:
			print("Caso {0}: 1 numero".format(count))
			print("0")
		else:
			print("Caso {0}: {1} numeros".format(count,1+N*(1+N)//2))
			print('0 ' + ' '.join([str(k) for k in range(N+1) for w in range(k)]))

		print()
		count += 1

	except:
		break
