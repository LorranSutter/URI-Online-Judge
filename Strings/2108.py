biggestWord = ''
biggestWordSize = 0

while True:
	S = input()

	if S == '0':
		break

	S = S.split()

	res = ''
	for k in S:
		l = len(k)
		if l >= biggestWordSize:
			biggestWord = k
			biggestWordSize = l
		res += str(l) + '-'

	print(res[:-1])

print()
print("The biggest word: " + biggestWord)
