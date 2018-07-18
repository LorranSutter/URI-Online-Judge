num = 0
count = 0
while True:
	try:
		S = input()
		num += int(input())
		count += 1
	except:
		print("{0:.1f}".format(num/count))
		break
