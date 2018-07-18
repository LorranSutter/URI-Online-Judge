for k in range(int(input())):
	D1 = int(input())
	D2, D3, D4, D5 = tuple(map(int,input().split()))
	D6 = int(input())

	if D1 + D6 != 7:
		print("NAO")
	elif D2 + D4 != 7:
		print("NAO")
	elif D3 + D5 != 7:
		print("NAO")
	elif len(set([D1,D2,D3,D4,D5,D6])) != 6:
		print("NAO")
	elif 1 > D1 or D1 > 6:
		print("NAO")
	elif 1 > D2 or D2 > 6:
		print("NAO")
	elif 1 > D3 or D3 > 6:
		print("NAO")
	elif 1 > D4 or D4 > 6:
		print("NAO")
	elif 1 > D5 or D5 > 6:
		print("NAO")
	elif 1 > D6 or D6 > 6:
		print("NAO")
	else:
		print("SIM")
