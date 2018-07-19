from math import sqrt

def dist(x1,y1,x2,y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)

while True:
	L, C, R1, R2 = map(int,input().split())

	if L == 0 and C == 0 and R1 == 0 and R2 == 0:
		break

	D1, D2 = R1*2, R2*2

	if   D1 > L:
		print("N")
	elif D1 > C:
		print("N")
	elif D2 > L:
		print("N")
	elif D2 > C:
		print("N")
	elif dist(R1, R1, L-R2, C-R2) >= R1+R2:
		print("S")
	elif dist(R1, R1, L-R2, R2) >= R1+R2:
		print("S")
	elif dist(R1, R1, R2, C-R2) >= R1+R2:
		print("S")
	else:
		print("N")
