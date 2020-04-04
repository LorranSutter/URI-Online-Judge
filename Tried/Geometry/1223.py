# Wrong answer 10%

from math import sqrt

while True:
	try:
		smallest = 10000
		odd = False

		N = int(input())
		L, H = tuple(map(int,input().split()))

		Y0, Xf, Yf = tuple(map(int,input().split()))

		dx = L - Xf

		if dx < smallest: smallest = dx

		for k in range(N-1):
			Y1, Xf1, Yf1 = tuple(map(int,input().split()))

			if odd:
				dx = L - Xf1
				dy = abs((Y1-Yf1)*Xf + Xf1*Yf - Xf1*Y1) / sqrt((Y1-Yf1)**2 + Xf1*Xf1)
				odd = False
			else:
				dx = Xf1
				dy = abs((Y1-Yf1)*Xf + (Xf1-L)*Yf + L*Yf1 - Xf1*Y1) / sqrt((Y1-Yf1)**2 + (Xf1-L)**2)
				odd = True

			if dx < smallest: smallest = dx
			if dy < smallest: smallest = dy

			Y0, Xf, Yf = Y1, Xf1, Yf1

		print("{0:.2f}".format(smallest))

	except:
		break