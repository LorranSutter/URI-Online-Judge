for k in range(int(input())):
	B = int(input())
	Ad, Dd, Ld = tuple(map(int,input().split()))
	Ag, Dg, Lg = tuple(map(int,input().split()))

	Vd = (Ad + Dd)/2 + (B if Ld%2 == 0 else 0)
	Vg = (Ag + Dg)/2 + (B if Lg%2 == 0 else 0)

	if Vd > Vg:
		print("Dabriel")
	elif Vg > Vd:
		print("Guarte")
	else:
		print("Empate")
