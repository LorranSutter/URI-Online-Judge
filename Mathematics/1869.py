N = int(float(input()))

def convert(num):
	if num < 32 and num > 9:
		return chr(num+55)
	else:
		return str(num)

while N != 0:
	res = ""
	while True:
		if N >= 32:			
			res += convert(N%32)
		else:
			res += convert(N)
			break
		N = N//32

	print(res[::-1])
	N = int(float(input()))

print("0")
