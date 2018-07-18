for k in range(int(input())):
	Name = input()
	GD = float(input())
	N = list(map(float,input().split()))

	N.remove(max(N))
	N.remove(min(N))

	print("{0} {1:.2f}".format(Name, sum(N)*GD))
