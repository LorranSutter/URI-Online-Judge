S = input()

while S != "0+0=0":
	S = S[::-1]
	a, b = S.split('=')
	b, c = b.split('+')

	if int(a) == int(b) + int(c):
		print('True')
	else:
		print('False')

	S = input()

print('True')
