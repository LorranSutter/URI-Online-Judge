nums = [0 for k in range(2001)]

for k in range(int(input())):
	nums[int(input())] += 1

for k in range(2001):
	if nums[k] != 0:
		print("{0} aparece {1} vez(es)".format(k,nums[k]))
