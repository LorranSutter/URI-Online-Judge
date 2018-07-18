P = ("Rafael","Beto","Carlos")

for k in range(int(input())):
	x, y = tuple(map(int,input().split()))

	players = (9*x*x + y*y, 2*x*x + 25*y*y, -100*x + y*y*y)

	winner = players.index(max(players))

	print("{0} ganhou".format(P[winner]))
