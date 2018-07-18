
N = int(input())

while N != 0:
	problems_incorrect = dict()
	for k in range(26):
		problems_incorrect[chr(k+65)] = 0

	problems_correct = []
	solved = 0
	total = 0

	for k in range(N):
		S = input().split()
		if S[2] == "incorrect":
			problems_incorrect[S[0]] += 1
		elif S[0] not in problems_correct:
			problems_correct.append(S[0])
			solved += 1
			total += int(S[1])

	for k in problems_correct:
		total += 20*problems_incorrect[k]

	print("{0} {1}".format(solved,total))

	N = int(input())
