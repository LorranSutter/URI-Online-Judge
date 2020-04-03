crypt = ['GQaku','ISblv','EOYcmw','FPZdnx','JTeoy','DNXfpz','AKUgq','CMWhr','BLVis','HRjt']

for k in range(int(input())):
	res = ''
	num = 0
	limit = False
	for char in input():
		for w in range(10):
			if char in crypt[w]:
				res += str(w)
				num += 1
			if num >= 12:
				limit = True
				break
		if limit:
			break

	print(res)
