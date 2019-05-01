for k in range(int(input())):
	R, S = input().split()
	R, S = R.lower(), S.lower()

	if R == S:
		print("empate")
	elif R == "tesoura":
		if S == "papel" or S == "lagarto":
			print("rajesh")
		else:
			print("sheldon")
	elif R == "papel":
		if S == "pedra" or S == "spock":
			print("rajesh")
		else:
			print("sheldon")
	elif R == "pedra":
		if S == "lagarto" or S == "tesoura":
			print("rajesh")
		else:
			print("sheldon")
	elif R == "lagarto":
		if S == "spock" or S == "papel":
			print("rajesh")
		else:
			print("sheldon")
	elif R == "spock":
		if S == "tesoura" or S == "pedra":
			print("rajesh")
		else:
			print("sheldon")
