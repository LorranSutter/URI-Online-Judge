while True:
	try:
		R, L = input().split('+')
		L, J = L.split('=')

		if R == 'R':
			print(int(J)-int(L))
		elif L == 'L':
			print(int(J)-int(R))
		else:
			print(int(R)+int(L))
		
	except:
		break
