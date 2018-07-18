for k in range(int(input())):
	L = input()
	C = list(map(int,input().split()))

	if L == "min":
		print("Caso #{0}: {1}".format(k+1,int(min(C))))
	elif L == "max":
		print("Caso #{0}: {1}".format(k+1,int(max(C))))
	elif L == "mean":
		print("Caso #{0}: {1}".format(k+1,int(sum(C)/3)))
	elif L == "eye":
		print("Caso #{0}: {1}".format(k+1,int(0.3*C[0]+0.59*C[1]+0.11*C[2])))
