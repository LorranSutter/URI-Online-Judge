tot = 0
for k in range(int(input())):
	P1, P2 = input().split()

	if P1 == "1001":
		tot += 1.5*int(P2)
	elif P1 == "1002":
		tot += 2.5*int(P2)
	elif P1 == "1003":
		tot += 3.5*int(P2)
	elif P1 == "1004":
		tot += 4.5*int(P2)
	elif P1 == "1005":
		tot += 5.5*int(P2)

print("{0:.2f}".format(tot))
