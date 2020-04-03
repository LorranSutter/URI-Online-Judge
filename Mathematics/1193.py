N = int(input())

for k in range(N):
	num, base = input().split()

	print('Case ' + str(k+1) + ':')

	if base == 'dec':
		print(hex(int(num))[2:] + " hex")
		print(bin(int(num))[2:] + " bin")
	elif base == 'hex':
		print(str(int(num,16)) + " dec")
		print(bin(int(num, 16))[2:] + " bin")
	elif base == 'bin':
		print(str(int(num,2)) + " dec")
		print(hex(int(num, 2))[2:] + " hex")

	print()
