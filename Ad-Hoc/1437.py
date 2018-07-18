N = int(input())

while N != 0:
	sentido = 'N'
	S = input()

	for k in S:
		if sentido == 'N':
			if k == 'D': sentido = 'L'
			else: sentido = 'O'
		elif sentido == 'L':
			if k == 'D': sentido = 'S'
			else: sentido = 'N'
		elif sentido == 'S':
			if k == 'D': sentido = 'O'
			else: sentido = 'L'
		elif sentido == 'O':
			if k == 'D': sentido = 'N'
			else: sentido = 'S'

	print(sentido)

	N = int(input())
