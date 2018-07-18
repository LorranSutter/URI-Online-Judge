T = int(input())

while T != 0:
	sizes = [0 for k in range(T)]

	for k in range(T):
		Q, A, B = tuple(map(float,input().split()))
		sizes[k] = Q * (A+B)*5/2

	for k in range(T):
		print("Size #{0}:".format(k+1))
		print("Ice Cream Used: {0:.2f} cm2".format(sizes[k]))
	print()

	T = int(input())
