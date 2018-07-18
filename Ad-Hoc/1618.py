for k in range(int(input())):
	points = tuple(map(int,input().split()))

	if points[8] >= points[0] and \
	   points[8] <= points[2] and \
	   points[8] <= points[4] and \
	   points[8] >= points[6] and \
	   points[9] >= points[1] and \
	   points[9] >= points[3] and \
	   points[9] <= points[5] and \
	   points[9] <= points[7]:
	   print(1)
	else:
		print(0)
