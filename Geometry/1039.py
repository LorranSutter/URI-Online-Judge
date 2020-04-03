from math import sqrt

while True:
	try:
		R1, X1, Y1, R2, X2, Y2 = tuple(map(int,input().split()))

		if R1 >= sqrt((X2-X1)**2 + (Y2-Y1)**2) + R2:
			print("RICO")
		else:
			print("MORTO")
	except:
		break
