import math

while True:
	try:
		H, M = input().split()
		X = list(map(float,input().split()))
		l = len(X)

		Xm = sum(X)/l
		s = sum([(x - Xm)**2 for x in X])
		s = math.sqrt(s/(l-1))

		print("{0:.5f}".format(s))
	except:
		break
