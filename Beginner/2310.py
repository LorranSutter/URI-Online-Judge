St, Bt, At = 0, 0, 0
Ss, Bs, As = 0, 0, 0
for k in range(int(input())):
	N = input()
	S, B, A = tuple(map(int,input().split()))
	S1, B1, A1 = tuple(map(int,input().split()))

	St += S
	Bt += B
	At += A

	Ss += S1
	Bs += B1
	As += A1

print("Pontos de Saque: {0:.2f} %.".format(Ss/St * 100))
print("Pontos de Bloqueio: {0:.2f} %.".format(Bs/Bt * 100))
print("Pontos de Ataque: {0:.2f} %.".format(As/At * 100))
