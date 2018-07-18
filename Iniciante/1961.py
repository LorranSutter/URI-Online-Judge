P, N = tuple(map(int,input().split()))
S = tuple(map(int,input().split()))
win = True

for k in range(1,N):
	if abs(S[k]-S[k-1]) > P:
		win = False
		break

if win:
	print("YOU WIN")
else:
	print("GAME OVER")
