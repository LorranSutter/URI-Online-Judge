three = ['A', 'E', 'I', 'O', 'S', 'a', 'e', 'i', 'o', 's']

for k in range(int(input())):
	res = 1
	for w in input():
		if w in three:
			res *= 3
		else:
			res *= 2

	print(res)
