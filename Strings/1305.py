while True:
	try:
		num = input().split('.')
		cutoff = input().split('.')

		if len(num) == 1:
			num.append('')

		if num[0] == '':
			num[0] = 0

		mantissa = min(len(num[1]),len(cutoff[1]))

		num[1], cutoff[1] = num[1][:mantissa], cutoff[1][:mantissa]
		num[0], num[1] = int(num[0]), float('0.' + num[1])
		cutoff = float('0.' + cutoff[1])

		if num[1] >= cutoff and mantissa != 0:
			print(num[0] + 1)
		else:
			print(num[0])
	
	except:
		break
