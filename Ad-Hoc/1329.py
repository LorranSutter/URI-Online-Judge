N = int(input())

while N != 0:
	tot = sum(tuple(map(int,input().split())))
	print("Mary won {0} times and John won {1} times".format(N-tot,tot))
	
	N = int(input())
